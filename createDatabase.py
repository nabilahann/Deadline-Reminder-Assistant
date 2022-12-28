import sqlite3

conn = sqlite3.connect('HCNBot.db')
c = conn.cursor()
c.execute("DROP TABLE daftarTask")
c.execute("""CREATE TABLE daftarTask (
            tanggal text,
            kode text,
            jenis text,
            topik text
)""")

input5 = ('13/12/2020', 'IF2230', 'Tucil', 'STRING MATCHING')
input6 = ('25/04/2021', 'IF2230', 'Tubes', 'PEMANASAN GLOBAL')
input7 = ('28/04/2021', 'IF2240', 'Tugas', 'TEORI EVOLUSI DARWIN')
input8 = ('29/04/2021', 'IF2250', 'Kuis', 'SISTEM TATA SURYA')
input9 = ('22/05/2021', 'IF2230', 'UAS', 'POLUSI CAHAYA')
input10 = ('01/05/2021', 'IF2230', 'Tugas', 'JAVA')
c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input5)
c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input6)
c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input7)
c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input8)
c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input9)
c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input10) 

c.execute("SELECT rowid, * FROM daftarTask")
data = c.fetchall()
print(data)

""" 
#create dummy data

input5 = ('13/12/2020', 'IF2230', 'Tucil', 'STRING MATCHING')
input6 = ('25/04/2021', 'IF2230', 'Tubes', 'ENGIMON')
input7 = ('28/04/2021', 'IF2240', 'Tugas', 'STRING MATCHING')
input8 = ('29/04/2021', 'IF2250', 'Kuis', 'ENGIMON')
input9 = ('22/05/2021', 'IF2230', 'UAS', 'STRING MATCHING')
input10 = ('01/05/2021', 'IF2230', 'Tugas', 'ENGIMON')
c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input5)
c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input6)
c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input7)
c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input8)
c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input9)
c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input10) 

"""



'''
conn = sqlite3.connect('HCNBot.db')
c = conn.cursor()

# contoh masukin data ke database

input = ('tanggal','kode','jenis','topik')
c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input)

# contoh ambil data

c.execute("SELECT * FROM daftarTask WHERE tanggal = (?)", (tanggal,))
data = c.fetchall()

# untuk dapetin data diantara 2 tanggal 
t1 = 20210301 #cara buat gini pake fungsi convertTanggal
t = 20210430
c.execute("SELECT * FROM daftarTask where substr(tanggal,7,4)||substr(tanggal,4,2)||substr(tanggal,1,2) between (?) and (?)", (t1,t,))
data = c.fetchall()
print(data)

#untuk dapetin data pake ID nya
c.execute("SELECT rowid, * FROM daftarTask")
data = c.fetchall()
print(data)

conn.commit()
conn.close()

'''

conn.commit()
conn.close()