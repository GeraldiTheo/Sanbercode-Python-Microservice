from mysql.connector import connect

db = connect(
    host = 'localhost',
    user = 'geraldi',
    passwd = 'geraldi',
    database = 'rentalfilm'
)

print(db)

# Melihat Data
cursor = db.cursor()

query = 'SELECT * FROM customers'

cursor.execute(query)

data = cursor.fetchall()

for datum in data:
    print(datum)
    
# Manipulasi Data
cursor = db.cursor()

input_namaid = input("Input Nama Panggilan : ")
input_namalengkap = input("Input Nama Lengkap :")
input_email = input("Input Email :")

query = " INSERT INTO customers (namaid, namalengkap, email) VALUES('{}', '{}', '{}') ".format(input_namaid, input_namalengkap, input_email)

cursor.execute(query)

db.commit()

print(input_namaid, input_namalengkap, input_email)