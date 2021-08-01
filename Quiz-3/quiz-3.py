from mysql.connector import connect, cursor

# Essay 1

# Tulislah kode python untuk membuat database mysql dengan ketentuan:
# 1. nama database = awalan email, misal email kalian test01_man@gmail.com maka database = test01
# 2. buat kode yang lengkap dalam satu file python (import library, koneksi, dbs) dan salin kedalam jawaban


# db = connect(
#     host = 'localhost',
#     user = 'geraldi',
#     password = 'geraldi',
# )

# db_cursor = db.cursor()

# query = 'CREATE DATABASE geralditheo'
# db_cursor.execute(query)

# Essay 2

# Tulislah kode python untuk membuat table mysql dengan ketentuan:
# 1. koneksikan pada database yang dibuat pada soal essay 1
# 2. Check terlebih dahulu apakah ada table dengan nama yang sama
# 3. bua table dengan dengan nama siswa, dengan schema seperti berikut:
#   idsiswa = primary key, Auto Increment, Integer
#   namasiswa = String, Not Null
#   kelas = String, Not Null
#   nilairataan = FLoat
# 4. buat kode yang lengkap dalam satu file python (import library, koneksi, dbs) dan salin kedalam jawaban

# from mysql.connector import connect, cursor

# db = connect(
#     host = 'localhost',
#     user = 'geraldi',
#     password = 'geraldi',
#     database = 'geralditheo'
# )

# db_cursor = db.cursor()

# query = 'SHOW DATABASES'
# db_cursor.execute(query)

# for x in db_cursor:
#     if 'siswa' in x:
#         print("The Table already there")
    

# query = 'CREATE TABLE siswa( idsiswa INT AUTO_INCREMENT PRIMARY KEY, namasiswa VARCHAR(255) NOT NULL , kelas VARCHAR(255) NOT NULL , nilairataan FLOAT )'
# db_cursor.execute(query)

# Essay 3

# tuliskan kode untuk memasukkan data di atas kedalam database dan table yang telah dibuat sebelumnya , ketentuannya adalah
# 1. Koneksikan dengan table yang sudah dibuat pada essay nomor 2
# 2. Masukkan data nama pada kolom namasiswa
# 3. Masukkan data tingkat dan kelas kolom kelas, misal tingkat 1 dan kelas C menjadi "1C" pada kolom kelas
# 4. Hitung rata rata nilai dan masukkan pada kolom nilai rataan
# 5. buat kode yang lengkap dalam satu file python (import library, koneksi, dbs) dan salin kedalam jawaban

# from mysql.connector import connect, cursor

# db = connect(
#     host = 'localhost',
#     user = 'geraldi',
#     password = 'geraldi',
#     database = 'geralditheo'
# )

# db_cursor = db.cursor()

# data=[ 
#       { "nama":"Rudi", "tingkat":2, "kelas":"A", "nilai":[{ "matematika":89, "biologi":70, "fisika":78, "kimia":90 }] }, 
#       { "nama":"Nina", "tingkat":2, "kelas":"B", "nilai":[{ "matematika":91, "biologi":60, "fisika":60, "kimia":85 }] }, 
#       { "nama":"Mira", "tingkat":2, "kelas":"A", "nilai":[{ "matematika":78, "biologi":72, "fisika":76, "kimia":78 }] } 
#     ]

# for datum in data:
#     nama = datum['nama']
#     kelas = str(datum['tingkat']) + datum['kelas']
#     rataan = 0.0
#     for nilai in datum["nilai"]:
#         rataan = nilai['matematika'] + nilai['biologi'] + nilai['fisika'] + nilai['kimia']
    
#     rataan = rataan / 4
    
#     print(nama, kelas, rataan)
    
#     query = "INSERT INTO siswa (namasiswa, kelas, nilairataan) VALUES( '{}', '{}', {} )".format(nama, kelas, rataan)
#     db_cursor.execute(query)
#     db.commit()
    