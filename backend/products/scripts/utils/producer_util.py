import pika, json


class Publisher:
    def __init__(self, uri: str) -> None:
        self.uri = uri
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(uri))
        self.channel = self.connection.channel()

    def publish(self, method, body):
        try:
            properties = pika.BasicProperties(method)
            self.channel.basic_publish(
                exchange="",
                routing_key="main",
                body=json.dumps(body),
                properties=properties,
            )
        except Exception as e:
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(self.uri)
            )
            self.channel = self.connection.channel()
            properties = pika.BasicProperties(method)
            self.channel.basic_publish(
                exchange="",
                routing_key="main",
                body=json.dumps(body),
                properties=properties,
            )
