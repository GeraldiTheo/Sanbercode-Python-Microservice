from pymongo import MongoClient

class database:
    def __init__(self):
        try:
            self.nosql_db = MongoClient()
            self.db = self.nosql_db['perpustakaan']
            self.mongo_col = self.db.books
            
            print('Database Connected')
        except Exception as e:
            print(e)
    
    def showBooks(self):
        return self.mongo_col.find()
    
    
    def showBooksById(self, key):
        return self.mongo_col.find({'id': key})
    
    def searchBookByName(self, key):
        query = {"nama" : {"$regex": key, "$options": "i"}}
        result = self.mongo_col.find(query)
        return result
    
    def insertBook(self, document):
        self.mongo_col.insert_one(document)
    
    def updateBookById(self, key, update):
        self.mongo_col.update(
            {'id':key},
            {
                'id': key,
                'nama': update['nama'], 
                'pengarang': update['pengarang'], 
                'tahunterbit': update['tahunterbit'], 
                'genre': update['genre']
            }
        )
    
    def deleteBookById(self, key):
        self.mongo_col.remove({'id': key})