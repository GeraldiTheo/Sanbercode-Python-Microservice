from pymongo import MongoClient
from models.books import database as db
import csv

def show_all_book():
    books = db.showBooks()
    for book in books:
        print(book)

def add_book():
    data = open("bestsellers-with-categories.csv",encoding='utf-8')
    books = csv.reader(data, delimiter=',')
    next(books)
    
    i = 0

    for book in books:
        try:
            
            i += 1
            
            data = {
                'id': i,
                "nama": book[0],
                "pengarang": book[1],
                "tahunterbit": book[5],
                "genre": book[6]
            }
            
            db.insertBook(data)
            
        except Exception as e:
            print("Kesalahan pada saat memasukan data: {}".format(e))
            break

def search_book_by_id(params):
    books = db.showBooksById(params)
    
    for book in books:
        print(book)

def search_books(params):
    for book in db.searchBookByName(params):
        print(book)
        
        
def update_book_by_id(params, update):
    db.updateBookById(params, update)
    
    print('Update Finished')

def delete_book(params):
    db.deleteBookById(params)

if __name__ == "__main__":
    db = db()
    
    #### function
    # show_all_book()
    # add_book()
    # search_book_by_id(346)
    # search_books('geraldi')
    # update_book_by_id(346, {'nama': 'Geraldi', 'pengarang':' Theo', 'tahunterbit': '2011', 'genre': 'Fantasy'})
    # delete_book(346)
    
    
    db.nosql_db.close()