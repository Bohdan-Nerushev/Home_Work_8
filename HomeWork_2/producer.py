# producer.py
import pika
import json
from faker import Faker
from models import Contact

# Налаштування RabbitMQ
rabbitmq_host = 'localhost'  # Замініть на вашу адресу RabbitMQ, якщо потрібно
queue_name = 'email_queue'

# Налаштування Faker для генерації фейкових контактів
fake = Faker()

def create_fake_contacts(n):
    contacts = []
    for _ in range(n):
        contact = Contact(
            full_name=fake.name(),
            email=fake.email()
        )
        contact.save()
        contacts.append(str(contact.id))  # Додаємо ObjectID в список
    return contacts

def send_message_to_queue(contact_ids):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)

    for contact_id in contact_ids:
        channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=json.dumps({'contact_id': contact_id})
        )
        print(f"Sent {contact_id} to queue")
    
    connection.close()

if __name__ == '__main__':
    contact_ids = create_fake_contacts(10)  # Генеруємо 10 контактів
    send_message_to_queue(contact_ids)
