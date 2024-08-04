#seeds.py
from models import Authors, Qoutes
import connect
import json

# === === === Authors === === === #

with open('authors.json', 'r', encoding = 'utf-8') as f:
    date_list_authors = json.load(f)
        
for i in date_list_authors:
    Authors(
        fullname = i.get('fullname'),
        born_date = i.get('born_date'),
        born_location = i.get('born_location'),
        description = i.get('description')
        ).save()
    
# === === === Qoutes === === === #

with open('qoutes.json', 'r', encoding = 'utf-8') as f:
    quotes_data = json.load(f)
    for quote_data in quotes_data:
        author_name = quote_data.pop('author')
        author = Authors.objects(fullname=author_name).first()
        if author:
            quote = Qoutes(author=author, **quote_data)
            quote.save()
