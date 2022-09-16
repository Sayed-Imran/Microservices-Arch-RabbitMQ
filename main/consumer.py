import pika,json
from dotenv import load_dotenv
load_dotenv()
from scripts.db.mongo import mongo_client
from scripts.constants.app_configuration import MicroService
from scripts.db.mongo.microservice2.collections.product import Products
from scripts.db.mongo.microservice2.collections.productUser import ProductUser


connection = pika.BlockingConnection(pika.ConnectionParameters(MicroService.RabbitMQ.uri))
channel = connection.channel()
channel.queue_declare(queue="main")


product_db = Products(mongo_client)
product_user_db = ProductUser(mongo_client)

def callback(ch, method, properties, body):
    print("Received at main")
    data = json.loads(body)
    if properties.content_type == 'product_created':
        del data['likes']
        product_db.create_product(data)
        product_user_db.create_product({"product_id":data['product_id'],"users":[]})

    elif properties.content_type == 'product_detail_updated':
        product_db.update_product(data['product_id'],data)

    elif properties.content_type == 'product_deleted':
        product_db.delete_product(data['product_id'])
        product_user_db.delete_product(data['product_id'])


channel.basic_consume(queue="main", on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
