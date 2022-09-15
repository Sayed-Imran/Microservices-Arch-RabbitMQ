import pika
import json
from product_handler import ProductsHandler
connection = pika.BlockingConnection(pika.URLParameters("3.110.92.250"))

channel = connection.channel()

channel.queue_declare(queue="main")
product_handler = ProductsHandler()

def callback(ch, method, body, properties):
    print("Recieved in main")
    data = json.loads(body)

    if properties.content == 'product_created':
        del data['likes']
        product_handler.create_one(data)

    elif properties.content == 'product_updates':
        product_handler.update_one(data['product_id'],data)

    elif properties.content == 'product_delete':
        product_handler.delete_one(data['product_id'])


channel.basic_consume(queue="main", on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
