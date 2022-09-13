import pika


connection = pika.BlockingConnection(pika.URLParameters("65.0.110.171"))

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, body,properties):
    print("Recieved in main")
    print(body)

channel.basic_consume(queue='main',on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()