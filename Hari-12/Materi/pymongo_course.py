from pymongo import MongoClient

nosql_db = MongoClient()
db = nosql_db.bios
mongo_doc = db.customers

print(mongo_doc)

# Membaca Data

query = {
    'awards.year': { '$gt':1990, '$lt':2000 },
    'contribs': 'OOP'
}

result = mongo_doc.find(query)

for data in result:
    print(data)
    
# Manipulasi Data : Insert

# data = {}
# mongo_doc.insert_one(data)
# data = [{}]
# mongo_doc.insert_many(data)

# Manipulasi Data : Update

# mongo_doc.update({query syarat}, {nilai pengganti})

# Manipulasi Data : Delete

# mongo_doc.delete({syarat})
    
nosql_db.close()