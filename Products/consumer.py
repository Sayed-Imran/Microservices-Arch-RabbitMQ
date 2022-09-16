from math import prod
import pika, json
from dotenv import load_dotenv
load_dotenv()

from scripts.constants.app_configuration import MicroService
from scripts.core.handlers.product_handler import ProductsHandler
connection = pika.BlockingConnection(pika.ConnectionParameters(MicroService.RabbitMQ.uri))

channel = connection.channel()
channel.queue_declare(queue='admin')
product_handler = ProductsHandler()


def callback(ch, method, properties, body):
    print("Recieved in admin")
    product_id = json.loads(body)['product_id']
    product = product_handler.find_one(product_id)
    if properties.content_type == 'product_liked':
        product['likes'] += 1
        print('product_id',product_id)
        product_handler.update_one(product_id,product)
    elif properties.content_type == 'product_disliked':
        product['likes'] -=1
        print('product_id',product_id)
        product_handler.update_one(product_id,product)
    else:
        print("Invalid Content Type")

channel.basic_consume(queue='admin',on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()