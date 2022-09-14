import pika


connection = pika.BlockingConnection(pika.URLParameters("3.110.92.250"))

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print("Recieved in admin")

channel.basic_consume(queue='admin',on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()