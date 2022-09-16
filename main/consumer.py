import pika,json
from dotenv import load_dotenv
load_dotenv()
from scripts.constants.app_configuration import MicroService
from scripts.core.handlers.product_handler import ProductsHandler
from scripts.core.handlers.productUser_handler import ProductUserHandler



connection = pika.BlockingConnection(pika.ConnectionParameters(MicroService.RabbitMQ.uri))

channel = connection.channel()

channel.queue_declare(queue="main")
product_handler = ProductsHandler()
product_user_handler = ProductUserHandler()

def callback(ch, method, properties, body):
    print("Received at main")
    data = json.loads(body)
    if properties.content_type == 'product_created':
        del data['likes']
        product_handler.create_one(data)
        product_user_handler.productUser.create_product({"product_id":data['product_id'],"users":[]})

    elif properties.content_type == 'product_updated':
        product_handler.update_one(data['product_id'],data)

    elif properties.content_type == 'product_deleted':
        product_handler.delete_one(data['product_id'])
        product_user_handler.delete_product(data['product_id'])


channel.basic_consume(queue="main", on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
