import pika


connection = pika.BlockingConnection(pika.URLParameters("65.0.110.171"))

channel = connection.channel()


def publish():
    channel.basic_publish(exchange="", routing_key="admin", body="")
