
import random
import csv

def doubleChecker(a, b):
    if(a in b):
        return 0
    else:
        return 1

a = "aku makan manusia"
b = ["aku makan donat", "donat makan aku", "manusia makan aku"]

#print(doubleChecker(a,b))


def randomGenerator(moduler,minx):
    acak = -100
    while(acak < minx):
        acak = random.randint(1,11111)%moduler
    return acak

#print(randomGenerator(10))


def soalGenerator(level,moduler1, moduler2, minx1,minx2):
    kuncijawaban = ""
    operator = 0
    while(operator == 0):
        operator = level
    operand1 = randomGenerator(moduler1,minx1)
    operand2 = randomGenerator(moduler2,minx2)
    if(operator == 1):
        result = operand1 + operand2
        kuncijawaban = str(operand1) + " + " + str(operand2) + " " + str(result)
    elif(operator == 2):
        result = operand1 - operand2
        kuncijawaban = str(operand1) + " - " + str(operand2) + " " + str(result)
    elif(operator == 3):
        result = operand1 * operand2
        kuncijawaban = str(operand1) + " x " + str(operand2) + " " + str(result)
    elif(operator == 4):
        while(operand2 == 0):
            operand2 = randomGenerator(moduler2,minx2)
        result = operand1 / operand2
        kuncijawaban = str(operand1) + " / " + str(operand2) + " " + str(result)

    return kuncijawaban

#print(soalGenerator(4,10))

def soalCollector(level,moduler1, moduler2, minx1,minx2, maxsoal):
    banksoal = []
    while(len(banksoal)<maxsoal):
        kuncijawaban = soalGenerator(level,moduler1, moduler2, minx1,minx2)
        if(doubleChecker(kuncijawaban,banksoal) == 1):
            banksoal.append(kuncijawaban)
            #print(banksoal)
    return banksoal

#print(soalCollector(1,10,5))

def stringToList(string):
    li = list(string.split(" "))
    return li

def soalFormatter(banksoal,baris):
    kolom = []
    for x in range(len(banksoal)):
        kolom = stringToList(banksoal[x])
        #print("kolom")
        baris.append(kolom)
    return baris

#print(soalFormatter(soalCollector(3,11,15)))

def csvMaker(baris, namaoutput):
    with open(namaoutput, 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(["operand1","operator","operand2","hasil"])
        for x in range(len(baris)):
            writer.writerow(baris[x])
    csvFile.close()

#csvMaker(soalFormatter(soalCollector(3,11,20)))


def main():
    flag = 1
    baris = []
    while(flag == 1):
        print("selamat datang di program soal generator")
        print("tingkat kesulitan: ")
        print("1 -> operator yang digunakan ( + )")
        print("2 -> operator yang digunakan ( - )")
        print("3 -> operator yang digunakan ( * )")
        print("4 -> operator yang digunakan ( / )")
        level = int(input("Masukkan tingkat kesulitan : ")) + 1
        moduler1 = int(input("Masukkan angka maksimal operand 1 : ")) + 1
        moduler2 = int(input("Masukkan angka maksimal operand 2 : ")) + 1
        maxsoal = int(input("Masukkan banyak soal yang akan dibuat : "))
        minx1 = int(input("Masukkan minimal angka operand1 : "))
        minx2 = int(input("Masukkan minimal angka operand2 : "))

        baris = soalFormatter(soalCollector(level, moduler1, moduler2, minx1, minx2, maxsoal),baris)
        print("mau membuat soal lagi? ")
        flag = int(input("0 = No, 1 = Yes :  "))

    namaoutput = str(input("Masukkan nama file output dengan akhiran csv ( contoh bintang.csv ) : "))
    csvMaker(baris, namaoutput)
    print("Csv telah dibuat!")

    print("Terimakasih!")


baris = []
# baris = soalFormatter(soalCollector(1, 9, 9, 0, 0, 4),baris)
# baris = soalFormatter(soalCollector(1, 99, 9, 10, 0, 4),baris)
# baris = soalFormatter(soalCollector(2, 9, 9, 0, 0, 4),baris)
# baris = soalFormatter(soalCollector(2, 99, 9, 10, 0, 4),baris)
# baris = soalFormatter(soalCollector(1, 999, 99, 100, 10, 1),baris)
# baris = soalFormatter(soalCollector(2, 999, 99, 100, 10, 1),baris)
# baris = soalFormatter(soalCollector(1, 999, 999, 100, 100, 1),baris)
# baris = soalFormatter(soalCollector(2, 999, 999, 100, 100, 1),baris)
#
# baris = soalFormatter(soalCollector(1, 9, 9, 0, 0, 4),baris)
# baris = soalFormatter(soalCollector(1, 99, 9, 10, 0, 4),baris)
# baris = soalFormatter(soalCollector(2, 9, 9, 0, 0, 4),baris)
# baris = soalFormatter(soalCollector(2, 99, 9, 10, 0, 4),baris)
# baris = soalFormatter(soalCollector(1, 999, 99, 100, 10, 1),baris)
# baris = soalFormatter(soalCollector(2, 999, 99, 100, 10, 1),baris)
# baris = soalFormatter(soalCollector(1, 999, 999, 100, 100, 1),baris)
# baris = soalFormatter(soalCollector(2, 999, 999, 100, 100, 1),baris)
#
# baris = soalFormatter(soalCollector(1, 9, 9, 0, 0, 4),baris)
# baris = soalFormatter(soalCollector(1, 99, 9, 10, 0, 4),baris)
# baris = soalFormatter(soalCollector(2, 9, 9, 0, 0, 4),baris)
# baris = soalFormatter(soalCollector(2, 99, 9, 10, 0, 4),baris)
# baris = soalFormatter(soalCollector(1, 999, 99, 100, 10, 1),baris)
# baris = soalFormatter(soalCollector(2, 999, 99, 100, 10, 1),baris)
# baris = soalFormatter(soalCollector(1, 999, 999, 100, 100, 1),baris)
# baris = soalFormatter(soalCollector(2, 999, 999, 100, 100, 1),baris)
#
# baris = soalFormatter(soalCollector(1, 9, 9, 0, 0, 4),baris)
# baris = soalFormatter(soalCollector(1, 99, 9, 10, 0, 4),baris)
# baris = soalFormatter(soalCollector(2, 9, 9, 0, 0, 4),baris)
# baris = soalFormatter(soalCollector(2, 99, 9, 10, 0, 4),baris)
# baris = soalFormatter(soalCollector(1, 999, 99, 100, 10, 1),baris)
# baris = soalFormatter(soalCollector(2, 999, 99, 100, 10, 1),baris)
# baris = soalFormatter(soalCollector(1, 999, 999, 100, 100, 1),baris)
# baris = soalFormatter(soalCollector(2, 999, 999, 100, 100, 1),baris)
#
# csvMaker(baris, "kelas1.csv")

# baris = soalFormatter(soalCollector(1, 999, 99, 100, 10, 4),baris)
# baris = soalFormatter(soalCollector(1, 999, 999, 100, 100, 4),baris)
# baris = soalFormatter(soalCollector(2, 999, 99, 100, 10, 4),baris)
# baris = soalFormatter(soalCollector(2, 999, 999, 100, 100, 4),baris)
# baris = soalFormatter(soalCollector(1, 99, 9, 10, 0, 1),baris)
# baris = soalFormatter(soalCollector(2, 99, 9, 10, 0, 1),baris)
# baris = soalFormatter(soalCollector(2, 999, 999, 100, 100, 1),baris)
#
# baris = soalFormatter(soalCollector(1, 999, 99, 100, 10, 4),baris)
# baris = soalFormatter(soalCollector(1, 999, 999, 100, 100, 4),baris)
# baris = soalFormatter(soalCollector(2, 999, 99, 100, 10, 4),baris)
# baris = soalFormatter(soalCollector(2, 999, 999, 100, 100, 4),baris)
# baris = soalFormatter(soalCollector(1, 99, 9, 10, 0, 1),baris)
# baris = soalFormatter(soalCollector(2, 99, 9, 10, 0, 1),baris)
# baris = soalFormatter(soalCollector(2, 999, 999, 100, 100, 1),baris)
#
# baris = soalFormatter(soalCollector(1, 999, 99, 100, 10, 4),baris)
# baris = soalFormatter(soalCollector(1, 999, 999, 100, 100, 4),baris)
# baris = soalFormatter(soalCollector(2, 999, 99, 100, 10, 4),baris)
# baris = soalFormatter(soalCollector(2, 999, 999, 100, 100, 4),baris)
# baris = soalFormatter(soalCollector(1, 99, 9, 10, 0, 1),baris)
# baris = soalFormatter(soalCollector(2, 99, 9, 10, 0, 1),baris)
# baris = soalFormatter(soalCollector(2, 999, 999, 100, 100, 1),baris)
#
# baris = soalFormatter(soalCollector(1, 999, 99, 100, 10, 4),baris)
# baris = soalFormatter(soalCollector(1, 999, 999, 100, 100, 4),baris)
# baris = soalFormatter(soalCollector(2, 999, 99, 100, 10, 4),baris)
# baris = soalFormatter(soalCollector(2, 999, 999, 100, 100, 4),baris)
# baris = soalFormatter(soalCollector(1, 99, 9, 10, 0, 1),baris)
# baris = soalFormatter(soalCollector(2, 99, 9, 10, 0, 1),baris)
# baris = soalFormatter(soalCollector(2, 999, 999, 100, 100, 1),baris)
#
# csvMaker(baris, "kelas2.csv")

baris = soalFormatter(soalCollector(1, 999, 999, 100, 100, 2),baris)
baris = soalFormatter(soalCollector(2, 999, 999, 100, 100, 2),baris)
baris = soalFormatter(soalCollector(1, 9999, 999, 1000, 100, 2),baris)
baris = soalFormatter(soalCollector(2, 9999, 999, 1000, 100, 2),baris)
baris = soalFormatter(soalCollector(1, 9999, 9999, 1000, 1000, 2),baris)
baris = soalFormatter(soalCollector(2, 9999, 9999, 1000, 1000, 2),baris)
baris = soalFormatter(soalCollector(3, 99, 9, 10, 0, 1),baris)
baris = soalFormatter(soalCollector(3, 999, 9, 100, 0, 1),baris)
baris = soalFormatter(soalCollector(4, 99, 9, 10, 0, 1),baris)
baris = soalFormatter(soalCollector(4, 999, 9, 100, 0, 1),baris)
baris = soalFormatter(soalCollector(1, 99, 9, 10, 0, 1),baris)
baris = soalFormatter(soalCollector(2, 99, 9, 10, 0, 1),baris)
baris = soalFormatter(soalCollector(1, 999, 99, 100, 10, 1),baris)
baris = soalFormatter(soalCollector(2, 999, 99, 100, 10, 1),baris)

baris = soalFormatter(soalCollector(1, 999, 999, 100, 100, 2),baris)
baris = soalFormatter(soalCollector(2, 999, 999, 100, 100, 2),baris)
baris = soalFormatter(soalCollector(1, 9999, 999, 1000, 100, 2),baris)
baris = soalFormatter(soalCollector(2, 9999, 999, 1000, 100, 2),baris)
baris = soalFormatter(soalCollector(1, 9999, 9999, 1000, 1000, 2),baris)
baris = soalFormatter(soalCollector(2, 9999, 9999, 1000, 1000, 2),baris)
baris = soalFormatter(soalCollector(3, 99, 9, 10, 0, 1),baris)
baris = soalFormatter(soalCollector(3, 999, 9, 100, 0, 1),baris)
baris = soalFormatter(soalCollector(4, 99, 9, 10, 0, 1),baris)
baris = soalFormatter(soalCollector(4, 999, 9, 100, 0, 1),baris)
baris = soalFormatter(soalCollector(1, 99, 9, 10, 0, 1),baris)
baris = soalFormatter(soalCollector(2, 99, 9, 10, 0, 1),baris)
baris = soalFormatter(soalCollector(1, 999, 99, 100, 10, 1),baris)
baris = soalFormatter(soalCollector(2, 999, 99, 100, 10, 1),baris)

baris = soalFormatter(soalCollector(1, 999, 999, 100, 100, 2),baris)
baris = soalFormatter(soalCollector(2, 999, 999, 100, 100, 2),baris)
baris = soalFormatter(soalCollector(1, 9999, 999, 1000, 100, 2),baris)
baris = soalFormatter(soalCollector(2, 9999, 999, 1000, 100, 2),baris)
baris = soalFormatter(soalCollector(1, 9999, 9999, 1000, 1000, 2),baris)
baris = soalFormatter(soalCollector(2, 9999, 9999, 1000, 1000, 2),baris)
baris = soalFormatter(soalCollector(3, 99, 9, 10, 0, 1),baris)
baris = soalFormatter(soalCollector(3, 999, 9, 100, 0, 1),baris)
baris = soalFormatter(soalCollector(4, 99, 9, 10, 0, 1),baris)
baris = soalFormatter(soalCollector(4, 999, 9, 100, 0, 1),baris)
baris = soalFormatter(soalCollector(1, 99, 9, 10, 0, 1),baris)
baris = soalFormatter(soalCollector(2, 99, 9, 10, 0, 1),baris)
baris = soalFormatter(soalCollector(1, 999, 99, 100, 10, 1),baris)
baris = soalFormatter(soalCollector(2, 999, 99, 100, 10, 1),baris)

baris = soalFormatter(soalCollector(1, 999, 999, 100, 100, 2),baris)
baris = soalFormatter(soalCollector(2, 999, 999, 100, 100, 2),baris)
baris = soalFormatter(soalCollector(1, 9999, 999, 1000, 100, 2),baris)
baris = soalFormatter(soalCollector(2, 9999, 999, 1000, 100, 2),baris)
baris = soalFormatter(soalCollector(1, 9999, 9999, 1000, 1000, 2),baris)
baris = soalFormatter(soalCollector(2, 9999, 9999, 1000, 1000, 2),baris)
baris = soalFormatter(soalCollector(3, 99, 9, 10, 0, 1),baris)
baris = soalFormatter(soalCollector(3, 999, 9, 100, 0, 1),baris)
baris = soalFormatter(soalCollector(4, 99, 9, 10, 0, 1),baris)
baris = soalFormatter(soalCollector(4, 999, 9, 100, 0, 1),baris)
baris = soalFormatter(soalCollector(1, 99, 9, 10, 0, 1),baris)
baris = soalFormatter(soalCollector(2, 99, 9, 10, 0, 1),baris)
baris = soalFormatter(soalCollector(1, 999, 99, 100, 10, 1),baris)
baris = soalFormatter(soalCollector(2, 999, 99, 100, 10, 1),baris)


csvMaker(baris, "kelas3.csv")