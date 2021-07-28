from enum import unique
from mongoengine import connect, connection
from mongoengine import Document, StringField, IntField

connection = connect(db = 'perpustakaan', host = 'localhost', port = 27017)
        
if connection:
    print('MongoDB Success')

class Books(Document):
    userid = IntField(db_field='id')
    nama = StringField(required=True)
    pengarang = StringField(required=True)
    tahunterbit = StringField(required=True)
    genre = StringField(required=True)
    