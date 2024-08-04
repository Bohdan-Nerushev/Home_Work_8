# consumer.py
import pika
import json
from models import Contact

# Налаштування RabbitMQ
rabbitmq_host = 'localhost'  # Замініть на вашу адресу RabbitMQ, якщо потрібно
queue_name = 'email_queue'

def simulate_email_send(contact):
    # Імітація надсилання email
    print(f"Sending email to {contact.email}")

def callback(ch, method, properties, body):
    data = json.loads(body)
    contact_id = data['contact_id']
    
    contact = Contact.objects(id=contact_id).first()
    
    if contact and not contact.message_sent:
        simulate_email_send(contact)
        contact.message_sent = True
        contact.save()
        print(f"Updated contact {contact_id} to message_sent=True")

    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_consuming():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)
    
    print('Waiting for messages...')
    channel.start_consuming()

if __name__ == '__main__':
    start_consuming()
