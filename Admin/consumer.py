import pika
import json
from dotenv import load_dotenv
load_dotenv()

from scripts.core.handlers.product_handler import ProductsHandler
connection = pika.BlockingConnection(pika.ConnectionParameters("3.110.92.250"))

channel = connection.channel()

channel.queue_declare(queue="main")
product_handler = ProductsHandler()

def callback(ch, method, properties, body):
    data = json.loads(body)
    if properties.content_type == 'product_created':
        del data['likes']
        product_handler.create_one(data)

    elif properties.content_type == 'product_updated':
        product_handler.update_one(data['product_id'],data)

    elif properties.content_type == 'product_deleted':
        product_handler.delete_one(data['product_id'])


channel.basic_consume(queue="main", on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
