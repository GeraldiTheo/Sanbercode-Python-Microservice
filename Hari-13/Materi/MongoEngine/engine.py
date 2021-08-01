from mongoengine import connect
from mongoengine import Document, StringField, DynamicDocument

connection = connect(db="rentalfilm", host="localhost", port=27017)

if connection:
    print("MongoDB Connected")
    

class customers(Document):
    username = StringField(required=True, max_length=70)
    fullname = StringField(required=True, max_length=20)
    email = StringField(required=True, max_length=20)
    

# Membaca Data
for doc in customers.objects:
    print (doc.username, doc.fullname, doc.email)
    
for doc in customers.objects(username='Fernanda'):
    print (doc.username, doc.fullname, doc.email)
    
# Manipulasi Data

data = {
    "username" : 'Mary',
    "fullname" : 'Mary Marijoa', 
    "email" : 'mary@gmail.com'
}

# Insert

# customers(**data).save()

for doc in customers.objects:
    print (doc.username, doc.fullname, doc.email)
    
    
# Update

# doc_1 = customers.objects(username='Mary').first()
# print (doc_1.to_json())

# doc_1.username = 'MM'
# doc_1.save()

# Delete

# doc_1 = customers.objects(username='MM').first()
# doc_1.delete()