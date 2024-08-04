# models.py
from mongoengine import Document, StringField, BooleanField, connect

# Підключення до MongoDB
connect(db='homework', host='mongodb+srv://userHomeWork88:<password>@homework8.nr55k8x.mongodb.net/')

class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    message_sent = BooleanField(default=False)
