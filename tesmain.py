from main import *

#testing
def main():
    #testing ambil jenis task
    kata_penting = ["Kuis", "Ujian", "Tucil", "Tubes", "Praktikum", "Tugas Besar", "Tugas Kecil", "Latihan"]
    # input_user = "kuis IF2210 antara 15/04/2021 sampai 18/04/2021"
    # input_user2 = "kuis IF2210 tanggal 2012-09-12"
    # task = getJenisTask(kata_penting, input_user)
    # print(task)
    # tanggal, type_tanggal = getTanggal(input_user)
    # print(tanggal)
    # print("type : " + str(type_tanggal))
    # # testing regex kode matkul
    # course = findCourse("halohhalobandung")
    # print(course)
    # course = findCourse(input_user)
    # print(course)
    # #testing untuk topik
    # topik = findTopic("Untuk tanggal 14 April 2021 ada Tubes IF2211 topik String Matching")
    # print(topik)
    # topik = findTopic("Tubes IF2211 topik String Matching pada 2012-09-12")
    # #testing penentuan fitur
    # # findFitur("Tubes IF2211 topik String Matching pada 2012-09-12", kata_penting)
    # findFitur("Apa saja deadline sejauh ini?", kata_penting)
    # findFitur("Deadline tugas IF2211 itu kapan?", kata_penting)
    # findFitur("Deadline if2210 diundur menjadi 28/04/2021 kuis", kata_penting)
    # findFitur("Deadline task 4 diundur menjadi 28/04/2021", kata_penting)
    # findFitur("Saya sudah selesai mengerjakan if2211", kata_penting)
    # findFitur("Saya sudah selesai mengerjakan task 1", kata_penting)
    # findFitur("Apa yang bisa assistant lakukan?", kata_penting)
    # print("Urutan yang benar: add, detail, deadline, update, delete, help")

    # print(convertTanggal("15/04/2021"))
    # print(findID("Deadline task 111 diundur menjadi 28/04/2021"))

    # test, t1 = getTanggal("Deadline task 4 diundur menjadi 2021/04/29")
    # print(test)
    # # t = test[0][2]
    # # t2 = "20" + t
    # # print(t2)
    # print(toSaveTanggal(test[0], t1))
    print(findTopic("Deadline 14 April 2021 Tubes IF2211 topik String Matching"))
    # findFitur("Hai bot, tolong ingetin kalau ada kuis IF3110 tentang Bab 2 sampai 3 pada 22/04/21", kata_penting)

if __name__ == '__main__':
    main()