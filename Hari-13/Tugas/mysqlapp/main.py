from models import Customers

def tampil_data():
    data = mysqldb.showUsers()
    for datum in data:
        print(datum.userid, datum.username, datum.namadepan, datum.namabelakang, datum.email)
        
def tampil_data_oleh_id(key):
    data = mysqldb.showUserById(key)
    for datum in data:
        print(datum.userid, datum.username, datum.namadepan, datum.namabelakang, datum.email)
        
def masukkan_data(**data):
    mysqldb.insertUser(**data)
    print('data telah ditambahkan')
    
    
def update_data_oleh_id(key, username):
    mysqldb.updateUserById(key, username)
    print('data telah diupdate')


def hapus_data_oleh_id(key):
    mysqldb.deleteUserById(key)
    print('data telah dihapus')
    
##########################
my_data = {
    'username' : 'RK',
    'namadepan' : 'Ravi', 
    'namabelakang' : 'Kumar',
    'email' : 'ravi@gmail.com'
}
##########################


if __name__ == '__main__':
    ### database
    mysqldb = Customers()
    
    ### tempat menaruh fungsi yang ingin dijalankan
    
    # tampil_data()
    # tampil_data_oleh_id(2)
    # masukkan_data(**my_data)
    # update_data_oleh_id(2, 'Shishi')
    # hapus_data_oleh_id(3)
    
