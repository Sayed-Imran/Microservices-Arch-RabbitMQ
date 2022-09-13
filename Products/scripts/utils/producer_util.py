import pika, json


connection = pika.BlockingConnection(pika.URLParameters("65.0.110.171"))

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange="", routing_key="main", body=json.dumps(body), properties=properties)
