from procedure import *
import sqlite3

def tambahTask(tanggal, tipe, kodemk, jenis, topik):
  conn = sqlite3.connect('HCNBot.db')
  c = conn.cursor()

  in_tanggal = toSaveTanggal(tanggal[0], tipe)

  newTask = (in_tanggal, kodemk[0].upper(), jenis, topik.upper())

  c.execute("SELECT rowid, * FROM daftarTask WHERE tanggal = (?) AND kode = (?) AND jenis = (?) AND topik = (?)", (newTask))
  data = c.fetchall()

  notif = ""
  if (len(data) == 0):
      c.execute("INSERT INTO daftarTask values (?,?,?,?)", newTask)
      conn.commit()

      c.execute("SELECT rowid, * FROM daftarTask WHERE tanggal = (?) AND kode = (?) AND jenis = (?) AND topik = (?)", (newTask))
      data = c.fetchall()[0]

      notif = "[TASK BERHASIL DICATAT]<br>(ID: " + str(data[0]) + ") " + data[1] + " - " + data[2] + " - " + data[3] + " - " + data[4]
  else:
      notif = "[TASK SUDAH PERNAH DITAMBAHKAN]"
  
  return notif

def menuBantuan(kata_penting):
    help_msg = "[Fitur]<br>"
    help_msg += "  1.\tMenambahkan task baru<br>"
    help_msg += "  2.\tMelihat daftar task<br>"
    help_msg += "  3.\tMenampilkan deadline suatu task<br>"
    help_msg += "  4.\tMemperbaharui deadline task<br>"
    help_msg += "  5.\tMenandai suatu task sudah selesai<br>"
    help_msg += "  6.\tMenampilkan menu bantuan<br><br>"
    help_msg += "[Daftar kata penting]<br>"
    for i in range(len(kata_penting)):
        help_msg += "  " + str(i+1) + ".\t" + kata_penting[i] + "<br>"
    
    return(help_msg)
