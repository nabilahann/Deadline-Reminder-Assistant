from flask import Flask, render_template, request
from procedure import *
from fitur23 import daftarTask, deadlineTugas
from fitur16 import *
from fitur45 import *

app = Flask(__name__)

def findFitur(input_user, kata_penting):
	text = ""
	kata_apa = ["sejauh ini", "semua", "seluruh", "segala"]
	kata_deadline = ["deadline"]
	#kata_periode = ["hari", "minggu"]
	#kata_kapan = ["kapan"]
	kata_ubah = ["undur", "majukan", "ubah", "ganti"]
	kata_selesai = ["selesai", "kelar", "hapus", "kumpul"]
	kata_bantuan = ["help", "command", "assistant", "bantuan", "fitur"]

	tanggal, tipe = getTanggal(input_user)
	periode, tipeperiode = getPeriode(input_user)
	kodemk = findCourse(input_user)
	jenis = getJenisTask(kata_penting, input_user)
	topik = findTopic(input_user)
	id = findID(input_user)

	apa = stringMatching(input_user, kata_apa) 
	deadline = stringMatching(input_user, kata_deadline)
	#periode = stringMatching(input_user, kata_periode)
	#kapan = stringMatching(input_user, kata_kapan)
	ubah = stringMatching(input_user, kata_ubah)
	selesai = stringMatching(input_user, kata_selesai)
	bantuan = stringMatching(input_user, kata_bantuan)
	match = 0
	if (ubah and len(tanggal) != 0 and (len(kodemk) != 0 or id != "")):
		# Panggil update task
		# print("Memperbarui task")
		text = perbaharuiTask(tanggal, tipe, kodemk, jenis, id)
		# print(text)
		match = 1
	elif (selesai and (len(kodemk) != 0 or id != "")):
		# Hapus task dari db
		# print("Data berhasil dihapus")
		text = finishTask(kodemk, jenis, id)
		match = 1
	elif (bantuan):
		# Panggil fitur menampilkan help
		# print("Menu bantuan")
		text = menuBantuan(kata_penting)
		match = 1
	elif (len(tanggal) != 0 and len(kodemk) != 0 and len(topik) != 0 and jenis != ""):
		# Panggil tambah task
		# print("Tambah task")
		text = tambahTask(tanggal, tipe, kodemk, jenis, topik)
		match = 1
	elif (len(kodemk) != 0 and jenis != "" and len(topik) == 0 and len(tanggal) == 0):
		# Panggil liat deadline
		# print("Menampilkan deadline")
		text = deadlineTugas(kodemk, jenis)
		match = 1
	elif (len(tanggal) != 0 or len(periode) != 0  or jenis != "" or (apa and deadline)):
		# Panggil daftar task
		# print("Menampilkan semua task")
		text = daftarTask(tanggal, tipe, jenis, periode, tipeperiode)
		match = 1
	if (match == 0):
		text = "Maaf, pesan tidak dikenali :("
	print(text)
	return text

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/get")
def get_bot_response():
	kata_penting = ["Kuis", "Ujian", "Tucil", "Tubes", "Praktikum", "Tugas"]
	userText = request.args.get('msg')
	return str(findFitur(userText, kata_penting))

if __name__ == "__main__":
	app.run(debug=True)