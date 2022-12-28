from BoyerMoore import bmMatch
import re
from io import StringIO

class StringBuilder:
     _file_str = None

     def __init__(self):
         self._file_str = StringIO()

     def Append(self, str):
         self._file_str.write(str)

     def __str__(self):
         return self._file_str.getvalue()

def getJenisTask(kata_penting, input_user):
    found = 0
    hasil = ""
    for task in kata_penting:
        found = bmMatch(input_user, task)
        if(found != -1):
            hasil = task
            break
    return hasil

def getTanggal(input_user):
    date_regex_dmy = "(0[1-9]|[12][0-9]|3[01])[-/.](0[1-9]|1[012])[-/.](19|20[0-9][0-9]|[0-9][0-9])"
    date_regex_mdy = "(0[1-9]|1[012])[-/.](0[1-9]|[12][0-9]|3[01])[-/.](19|20[0-9][0-9]|[0-9][0-9])"
    date_regex_ymd = "(19|20[0-9][0-9])[-/.](0[1-9]|[12][0-9]|3[01])[-/.](0[1-9]|1[012])"
    date_regex_month = "(0[1-9]|[12][0-9]|3[01]|[1-9])[- /.]([A-Za-z]*)[- /.](19|20[0-9][0-9])"

    tanggal = []
    type_tanggal = 0

    if(re.search(date_regex_dmy, input_user)) :
        tanggal = re.findall(date_regex_dmy, input_user)
        type_tanggal = 1
    elif(re.search(date_regex_mdy, input_user)) :
        tanggal = re.findall(date_regex_mdy, input_user)
        type_tanggal = 2
    elif(re.search(date_regex_ymd, input_user)) :
        tanggal = re.findall(date_regex_ymd, input_user)
        type_tanggal = 3
    elif(re.search(date_regex_month, input_user)):
        tanggal = re.findall(date_regex_month, input_user)
        type_tanggal = 7

    return (tanggal, type_tanggal)

def getPeriode(input_user):
    minggu = "([0-9]+|[Ss]e)[ ]*[Mm]inggu ke depan"
    hari = "([0-9]+|[Ss]e)[ ]*[Hh]ari ke depan"
    today = "[Hh]ari ini"

    tanggal = []
    type_tanggal = 0

    if(re.search(minggu, input_user)) :
        tanggal = re.findall(minggu, input_user)
        type_tanggal = 4
    elif(re.search(hari, input_user)) :
        tanggal = re.findall(hari, input_user)
        type_tanggal = 5
    elif(re.search(today, input_user)) :
        tanggal = re.findall(today, input_user)
        type_tanggal = 6

    return (tanggal, type_tanggal)

# coba regex kodematkul
def findCourse(string):
    courseRegex = '[A-Za-z][A-Za-z]\d\d\d\d'
    hasil = re.findall(courseRegex, string)
    return hasil

# temp topik, butuh testing lebih banyak
def findTopic(input_user):
    topicRegex = '(topik [A-Za-z\s1-9]*(\S|\spada))|(tentang [A-Za-z\s1-9]* (pada))'
    hasil = re.findall(topicRegex, input_user)
    print(hasil)
    if (bmMatch(input_user, "topik") != -1):
         hasil = hasil[0][0]
    elif (bmMatch(input_user, "tentang") != -1):
         hasil = hasil[0][2]

    if (hasil != []):
        hasil = hasil.split(" pada ")[0].replace("topik", "").replace("tentang", "").replace("pada", "").strip()
    return hasil

def findID(input_user):
    idRegex = '[Tt]ask [0-9][0-9][0-9]|[Tt]ask [0-9][0-9]|[Tt]ask [0-9]'
    hasil = re.findall(idRegex, input_user)
    find = ""
    # print(hasil)
    if (hasil != []):
        find = hasil[0]
        find = find.replace("task", "").replace("Task", "").strip()
    return find

def stringMatching(input_user, arrkata):
    value = False
    for kata in arrkata:
        if(bmMatch(input_user, kata) != -1):
            value = True
            break

    return value

def convertTanggal(tgl):
    hasil = ""
    sb = StringBuilder()
    sb.Append(tgl[6:10])
    sb.Append(tgl[3:5])
    sb.Append(tgl[0:2])
    hasil = str(sb)

    return hasil
    
def toSaveTanggal(tgl, tipe):
    tanggal = ""
    if (tipe == 1):
        if(len(tgl[2]) == 4):
            tanggal = tgl[0] + "/" + tgl[1] + "/" + tgl[2]
        else:
            t = "20" + tgl[2]
            tanggal = tgl[0] + "/" + tgl[1] + "/" + t
    elif (tipe == 2):
        if(len(tgl[2]) == 4):
            tanggal = tgl[1] + "/" + tgl[0] + "/" + tgl[2]
        else:
            t = "20" + tgl[2]
            tanggal = tgl[1] + "/" + tgl[0] + "/" + t
    elif (tipe == 3):
        tanggal = tgl[2] + "/" + tgl[1] + "/" + tgl[0]
    elif (tipe == 7):
        if (len(tgl[0]) == 1):
            ltgl = list(tgl)
            ltgl[0] = "0" + ltgl[0]
            tgl = tuple(ltgl)
          
        if (stringMatching(tgl[1].upper(), ["JANUARI"])):
            tanggal = tgl[0] + "/01/" + tgl[2]
        elif (stringMatching(tgl[1].upper(), ["FEBRUARI"])):
            tanggal = tgl[0] + "/02/" + tgl[2]
        elif (stringMatching(tgl[1].upper(), ["MARET"])):
            tanggal = tgl[0] + "/03/" + tgl[2]
        elif (stringMatching(tgl[1].upper(), ["APRIL"])):
            tanggal = tgl[0] + "/04/" + tgl[2]
        elif (stringMatching(tgl[1].upper(), ["MEI"])):
            tanggal = tgl[0] + "/05/" + tgl[2]
        elif (stringMatching(tgl[1].upper(), ["JUNI"])):
            tanggal = tgl[0] + "/06/" + tgl[2]
        elif (stringMatching(tgl[1].upper(), ["JULI"])):
            tanggal = tgl[0] + "/07/" + tgl[2]
        elif (stringMatching(tgl[1].upper(), ["AGUSTUS"])):
            tanggal = tgl[0] + "/08/" + tgl[2]
        elif (stringMatching(tgl[1].upper(), ["SEPTEMBER"])):
            tanggal = tgl[0] + "/09/" + tgl[2]
        elif (stringMatching(tgl[1].upper(), ["OKTOBER"])):
            tanggal = tgl[0] + "/10/" + tgl[2]
        elif (stringMatching(tgl[1].upper(), ["NOVEMBER"])):
            tanggal = tgl[0] + "/11/" + tgl[2]
        elif (stringMatching(tgl[1].upper(), ["DESEMBER"])):
            tanggal = tgl[0] + "/12/" + tgl[2]
            
    return tanggal
