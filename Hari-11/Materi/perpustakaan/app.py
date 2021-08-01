from models.customers import database

data = {
    "params":[
        {
            "values" :{
                "username" : "userpertama",
                "namadepan" : "rudi",
                "namabelakang" : "roundhouse",
                "email" : "rudi.roundhouse@gmail.com"
            } 
        },
        {
            "values" :{
                "username" : "userkedua",
                "namadepan" : "shiroe",
                "namabelakang" : "ishigami",
                "email" : "shiroe.ishigami@gmail.com"
            } 
        },
        {
            "values" :{
                "username" : "userketiga",
                "namadepan" : "akatsuki",
                "namabelakang" : "horizon",
                "email" : "akatsuki.horizon@gmail.com"
            } 
        }
    ]
}

detail = {
    "params":[
        {
            "userid": 2,
        }
    ]
}

def tampilData():
    data = mysqldb.showUsers()
    for datum in data:
        print(datum)
    print("data berhasil diperlihatkan")
    
def detailData(data):
    for param in data['params']:
        data = mysqldb.showUserById(**param)
        
    print(data)
    
    
    print("data berhasil dedetailkan")

def tambahData(data):
    for param in data['params']:
        mysqldb.insertUser(**param)
    mysqldb.dataCommit()
    print("data berhasil ditambahkan")

def ubahData(data):    
    for param in data['params']:
        mysqldb.updateUserById(**param)
    mysqldb.dataCommit()
    print("data berhasil diubah")

def hapusData(data):
    for param in data['params']:
        mysqldb.deleteUserById(**param)
    mysqldb.dataCommit()
    print("data berhasil dihapus")



if __name__ == "__main__":
    mysqldb = database()
    if mysqldb.db.is_connected():
        print('Connected to MySQL database')
    
    #isi dengan fungsi yang kalian butuhkan
    #jangan lupa untuk menyesuaikan isi variabel data dengan struktur data yang dibutuhkan
    
    # tampilData()
    # detailData(detail)
    # tambahData(data)
    # ubahData(detail)
    # hapusData(detail)
        
    if mysqldb.db is not None and mysqldb.db.is_connected():
        mysqldb.db.close()