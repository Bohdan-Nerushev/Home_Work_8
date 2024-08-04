from datetime import datetime

from mongoengine import  Document
from mongoengine.fields import BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField, ReferenceField


class Authors(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()
    
    
    meta = {'allow_inheritance': True}
    
class Qoutes(Document):
    tags = ListField(StringField())
    author = ReferenceField(Authors, required=True) 
    quote = StringField(required=True)

    meta = {'allow_inheritance': True}
