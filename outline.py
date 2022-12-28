import re


#input_user = str(input("Masukkan pesan: "))
input_user = "kuis antara 15/04/2021 sampai 18/04/2021"
kata_terbaca = input_user.split(" ") # ini bakal diganti algo string matching

kata_penting = ["Kuis", "Ujian", "Tucil", "Tubes", "Praktikum"]
date_regex_dmy = "(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d"
date_regex_mdy = "(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d"
#date_regex_spasi = "([1-9]|[12][0-9]|3[01]) ([jJ]anuari]) ([19|20][0-9][0-9])"

tugas_tercatat = [
    ["14/04/2021", "IF2211", "Tubes", "String matching"],
    ["15/04/2021", "IF2220", "Tucil", "Basis data"],
    ["16/04/2021", "IF2230", "Kuis", "Astronomi"]] # ini contoh yg udah kesimpan di file luar



"""
urutan prioritas:
-- update: diundur, dimajukan

-- selesai: selesai, kelar

-- help: help, commands, assistant

-- add: tanggal, kode matkul, jenis tugas (kata penting), topik (yang sesudahnya)

-- menampilkan
jenis task (kata penting): 3 minggu ke depan ada kuis apa saja: kuis
deadline tugas tertentu: tugas, IF2200
periode:
tanggal: "DATE_1" "DATE_2" (regex)
N minggu ke depan: minggu ke depan
N hari ke depan: hari ke depan
Hari ini: hari ini
(ketiganya bisa digabung)

semua task: "sejauh ini", "semua"

-- kata penting: yg di atas

-- bonus: kata mirip
"""

# ini testing regex tanggal

if re.search(date_regex_dmy, "28/12/2000"): # valid
    print("a")
if re.search(date_regex_dmy, "12/28/2000"): # invalid month
    print("b")
if re.search(date_regex_dmy, "04/05/2000"): # valid
    print("c")
if re.search(date_regex_dmy, "31/04/2000"): # invalid date for month
    print("g")
if re.search(date_regex_dmy, "29/02/2001"): # leap year invalid
    print("h")

if re.search(date_regex_mdy, "28/12/2000"): # invalid
    print("d")
if re.search(date_regex_mdy, "12/28/2000"): # valid
    print("e")
if re.search(date_regex_mdy, "04/05/2000"): # valid
    print("f")

# tanggal2 pengecualian di-hardcode aja

#contoh baca input user dan dapetin tanggal
# input_user = "kuis antara 15-04-2021 sampai 18/04/2021"
# input_user2 = "kuis 4 januari 2021"
# n = re.search(date_regex_spasi, input_user2)
# print(n.group(0))
# m = re.search(date_regex_dmy, input_user)
#print(m)
# p = re.findall(date_regex_mdy, input_user)
# print(p)
# kata = re.split(" ", input_user)
# print(kata)
# for i in kata:
#     match = re.search(date_regex_dmy, i)
#     #print(match)
#     if match :
#         print(match.group(0))

#print(tanggal)


