from procedure import *
import sqlite3


def perbaharuiTask(tanggal, type, kodemk, jenis, id):
    conn = sqlite3.connect('HCNBot.db')
    c = conn.cursor()

    text = ""
    ctgl = toSaveTanggal(tanggal[0], type)

    #kalo dikasih tau id task nya
    if(id != ""):
        c.execute("SELECT rowid, * FROM daftarTask WHERE rowid = (?)", (id,))
        data = c.fetchall()
        # print(data)
        if (data != []):
            update = """UPDATE daftarTask 
                        SET tanggal = ? 
                        WHERE rowid = ? """
            c.execute(update,(ctgl, id))
            c.execute("SELECT rowid, * FROM daftarTask WHERE rowid = (?)", (id,))
            data2 = c.fetchall()
            text = "[TASK BERHASIL DIPERBAHARUI]<br>"
            for i in range (len(data2)):
                text += (str(i+1)+". (ID: "+str(data2[i][0])+") "+data2[i][1]+" - "+data2[i][2]+" - "+data2[i][3]+" - "+data2[i][4])
                if (i != len(data2)-1):
                    text += "<br>"
        else :
            text = "[TASK GAGAL DIPERBAHARUI. ID TASK TIDAK DITEMUKAN]"
            # print("test")
    else :
        kode = kodemk[0].upper()
        #kalo cuma dikasih tau kode
        if(jenis == "" and len(kodemk) != 0):
            c.execute("SELECT * FROM daftarTask WHERE kode = (?)", (kode,))
            data = c.fetchall()
            # print(data)

            if (data != []):
                update = """UPDATE daftarTask 
                            SET tanggal = ? 
                            WHERE kode = ? """
                c.execute(update,(ctgl, kode))
                c.execute("SELECT rowid, * FROM daftarTask WHERE kode = (?)", (kode,))
                data2 = c.fetchall()
                text = "[TASK BERHASIL DIPERBAHARUI]<br>"
                for i in range (len(data2)):
                    text += (str(i+1)+". (ID: "+str(data2[i][0])+") "+data2[i][1]+" - "+data2[i][2]+" - "+data2[i][3]+" - "+data2[i][4])
                    if (i != len(data2)-1):
                        text += "<br>"
            else :
                text = "[TASK GAGAL DIPERBAHARUI. KODE MATA KULIAH TIDAK DITEMUKAN]"
                # print("test")
        #kalo cuma dikasih tau kode dan jenis
        elif(jenis != "" and len(kodemk) != 0):
            c.execute("SELECT * FROM daftarTask WHERE kode = (?) AND jenis = (?)", (kode,jenis,))
            data = c.fetchall()
            # print(data)
            # print("test1")
            if (data != []):
                update = """UPDATE daftarTask 
                            SET tanggal = ? 
                            WHERE kode = ? AND
                            jenis = ? """
                c.execute(update,(ctgl, kode, jenis))
                c.execute("SELECT rowid, * FROM daftarTask WHERE kode = (?) AND jenis = (?)", (kode,jenis,))
                data2 = c.fetchall()
                text = "[TASK BERHASIL DIPERBAHARUI]<br>"
                for i in range (len(data2)):
                    text += (str(i+1)+". (ID: "+str(data2[i][0])+") "+data2[i][1]+" - "+data2[i][2]+" - "+data2[i][3]+" - "+data2[i][4])
                    if (i != len(data2)-1):
                        text += "<br>"
            else :
                text = "[TASK GAGAL DIPERBAHARUI. TASK TIDAK DITEMUKAN]"
                # print("test")

    conn.commit()
    conn.close()

    return text

def finishTask(kodemk, jenis, id):
    conn = sqlite3.connect('HCNBot.db')
    c = conn.cursor()

    text = ""
    

    #kalo dikasih tau id task nya
    if(id != ""):
        c.execute("SELECT rowid, * FROM daftarTask WHERE rowid = (?)", (id,))
        data = c.fetchall()
        # print(data)

        if (data != []):
            c.execute("DELETE FROM daftarTask WHERE rowid = (?)", (id, ))
            text = "[TASK BERHASIL DIHAPUS]"
        else :
            text = "[TASK GAGAL DIHAPUS. ID TASK TIDAK DITEMUKAN]"
    #kalo cuma dikasih tau kode
    else:
        kode = kodemk[0].upper()
        if(jenis == "" and len(kodemk) != 0):
            c.execute("SELECT * FROM daftarTask WHERE kode = (?)", (kode,))
            data = c.fetchall()
            # print(data)

            if (data != []):
                c.execute("DELETE FROM daftarTask WHERE kode = (?)", (kode, ))
                text = "[TASK BERHASIL DIHAPUS]"
            else :
                text = "[TASK GAGAL DIHAPUS. KODE MATA KULIAH TIDAK DITEMUKAN]"
        #kalo cuma dikasih tau kode dan jenis
        elif(jenis != "" and len(kodemk) != 0):
            c.execute("SELECT * FROM daftarTask WHERE kode = (?) AND jenis = (?)", (kode,jenis,))
            data = c.fetchall()
            # print(data)

            if (data != []):
                c.execute("DELETE FROM daftarTask WHERE kode = (?) AND jenis = (?)", (kode,jenis,))
                text = "[TASK BERHASIL DIHAPUS]"
            else :
                text = "[TASK GAGAL DIHAPUS. KODE MATA KULIAH TIDAK DITEMUKAN]"

    conn.commit()
    conn.close()

    return text