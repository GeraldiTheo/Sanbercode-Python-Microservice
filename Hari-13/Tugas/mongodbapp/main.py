from models import Books

def lihat_document():
    for book in Books.objects:
        print(book.id, book.nama, book.pengarang, book.tahunterbit, book.genre)

def lihat_document_oleh_id(id):
    for book in Books.objects(userid = id):
        print(book.id, book.nama, book.pengarang, book.tahunterbit, book.genre)

def memasukkan_document(data):
    Books(**data).save()
    
def update_document(id, nama):
    datum = Books.objects(userid = id).first()
    
    datum.nama = nama
    
    datum.save()
    
def hapus_document(id):
    datum = Books.objects(userid = id).first()
    datum.delete()
    
######################
data = {
    'nama' : 'Geraldi',
    'pengarang' : 'Egoist',
    'tahunterbit' : '2021',
    'genre' : 'Horror'
}
######################

if __name__ == '__main__':
    
    # place the function here...
    
    print('Hello')
    
    # lihat_document()
    lihat_document_oleh_id(4) 
    # memasukkan_document(data)
    # update_document(4, 'Odore')
    # hapus_document(4)
    
    