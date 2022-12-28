import sqlite3
from procedure import convertTanggal, toSaveTanggal
from datetime import date, timedelta

def daftarTask(tanggal, tipetanggal, jenis, periode, tipeperiode):
    hasil = ""
    conn = sqlite3.connect('HCNBot.db')
    c = conn.cursor()
    if (jenis == ""):
        if (tipetanggal == 0 and tipeperiode == 0):
            # semua deadline total
            c.execute("SELECT rowid, * FROM daftarTask", ())
            data = c.fetchall()
        elif (tipeperiode == 4 or tipeperiode == 5):
            # periode tanpa jenis
            today = date.today()
            d1 = today.strftime("%Y%m%d")
            if periode[0] == "se" or "Se":
                periode[0] = 1
            if tipeperiode == 4:
                d2 = today + timedelta(days=int(periode[0])*7)
            elif tipeperiode == 5:
                d2 = today + timedelta(days=int(periode[0]))
            d2 = d2.strftime("%Y%m%d")
            arrtanggal = [d1, d2]
            c.execute("SELECT rowid, * FROM daftarTask where substr(tanggal,7,4)||substr(tanggal,4,2)||substr(tanggal,1,2) between (?) and (?)", arrtanggal)
            data = c.fetchall()
        elif (tipeperiode == 6):
            # hari ini tanpa jenis
            today = date.today()
            d1 = today.strftime("%d/%m/%Y")
            c.execute("SELECT rowid, * FROM daftarTask WHERE tanggal = (?)", (d1,))
            data = c.fetchall()
        else:
            # semua deadline dalam tanggal yang dipilih
            tgl1 = convertTanggal(toSaveTanggal(tanggal[0], tipetanggal))
            tgl2 = convertTanggal(toSaveTanggal(tanggal[1], tipetanggal))
            arrtanggal = [tgl1, tgl2]
            c.execute("SELECT rowid, * FROM daftarTask where substr(tanggal,7,4)||substr(tanggal,4,2)||substr(tanggal,1,2) between (?) and (?)", arrtanggal)
            data = c.fetchall()
    else: # jenis berisi
        if (tipetanggal == 0 and tipeperiode == 0):
            # semua deadline dengan kata tanpa tanggal
            c.execute("SELECT rowid, * FROM daftarTask WHERE jenis = (?)", (jenis,))
            data = c.fetchall()
        elif (tipeperiode == 4 or tipeperiode == 5):
            # periode dengan jenis
            today = date.today()
            d1 = today.strftime("%Y%m%d")
            if periode[0] == "se" or "Se":
                periode[0] = 1
            if tipeperiode == 4:
                d2 = today + timedelta(days=int(periode[0])*7)
            elif tipeperiode == 5:
                d2 = today + timedelta(days=int(periode[0]))
            d2 = d2.strftime("%Y%m%d")
            c.execute("SELECT rowid, * FROM daftarTask WHERE jenis = (?) and (substr(tanggal,7,4)||substr(tanggal,4,2)||substr(tanggal,1,2) between (?) and (?))", (jenis,d1,d2,))
            data = c.fetchall()
        elif (tipeperiode == 6):
            # hari ini dengan jenis
            today = date.today()
            d1 = today.strftime("%d/%m/%Y")
            c.execute("SELECT rowid, * FROM daftarTask WHERE jenis = (?) and tanggal = (?)", (jenis,d1,))
            data = c.fetchall()
        else:
            # semua deadline dengan kata dan tanggal yang dipilih
            tgl1 = convertTanggal(toSaveTanggal(tanggal[0], tipetanggal))
            tgl2 = convertTanggal(toSaveTanggal(tanggal[1], tipetanggal))
            c.execute("SELECT rowid, * FROM daftarTask WHERE jenis = (?) and substr(tanggal,7,4)||substr(tanggal,4,2)||substr(tanggal,1,2) between (?) and (?)", (jenis,tgl1,tgl2,))
            data = c.fetchall()
    if data == "Maaf, pesan tidak dikenali :(":
        hasil += data
    elif (len(data)==0):
        hasil += "Tidak ada"
    else:
        hasil += "[Daftar Deadline]<br>"
        for i in range (len(data)):
            hasil += (str(i+1)+". (ID: "+str(data[i][0])+") "+data[i][1]+" - "+data[i][2]+" - "+data[i][3]+" - "+data[i][4])
            if (i != len(data)-1):
                hasil += "<br>"
    conn.close()
    return hasil

def deadlineTugas(kodematkul, jenis):
    hasil = ""
    kode = kodematkul[0].upper()
    conn = sqlite3.connect('HCNBot.db')
    c = conn.cursor()
    c.execute("SELECT tanggal, topik FROM daftarTask WHERE kode = (?) and jenis = (?)", (kode,jenis,))
    data = c.fetchall()
    if (len(data)==0):
        hasil += "Tidak ada"
    else:
        for i in range (len(data)):
            hasil += data[i][0]+": "+data[i][1]
            if (i != len(data)-1):
                hasil += "<br>"
    return hasil

# driver
def main():
    conn = sqlite3.connect('HCNBot.db')
    c = conn.cursor()

    # disini makan nasi juga kata penting untuk keperluan testing

    # dummy, cukup sekali
    """ input1 = ('12/12/2012', 'IF1212', 'makan kerupuk', 'topik')
    input2 = ('12/12/2012', 'IF1212', 'makan nasi', 'topik')
    input3 = ('12/12/2012', 'IF1212', 'makan nasi lagi', 'topik')
    input4 = ('14/12/2012', 'IF1211', 'makan nasi lagi lagi', 'topik')
    input5 = ('13/12/2012', 'IF1211', 'makan nasi', 'topik')
    input6 = ('25/04/2021', 'IF1211', 'makan nasi lagi lagi', 'topik')
    input7 = ('28/04/2021', 'IF1211', 'makan nasi', 'topik')
    input8 = ('29/04/2021', 'IF1211', 'makan nasi aaa', 'topik')
    input9 = ('22/05/2021', 'IF1211', 'makan nasi', 'topik')
    c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input1)
    c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input2)
    c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input3)
    c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input4)
    c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input5)
    c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input6)
    c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input7)
    c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input8)
    c.execute("INSERT INTO daftarTask VALUES (?,?,?,?)", input9) """

    c.execute("SELECT * FROM daftarTask", ())
    data = c.fetchall()
    for i in range (len(data)):
        print(data[i])
    print()

    """ print(daftarTask([], 0, ""))
    print(daftarTask([], 0, "makan nasi"))
    print(daftarTask(["12", "12", "2012", "15", "12", "2012"], 1, ""))
    print(daftarTask(["12", "12", "2012", "13", "12", "2012"], 1, "makan nasi"))
    print(daftarTask(["30", "hari ke depan"], 4, "makan nasi"))
    print(deadlineTugas("IF1211", "makan nasi")) """

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()