# # NGECEK FUNGSI LEN UNTUK STRING
# x = 'Halo Dunia'
# print(len(x))

# # NGECEK FUNGSI LEN UNTUK LIST
# y = [1, 2, 3]
# print(len(y))

# # SOLVE 1 CARA 1
# x = 4
# y = 3
# z = 2

# w = ((x + y * z)/(x * y))**z

# print(w)

# # SOLVE 1 CARA 2
# def soal1(x,y,z):
#     w = ((x + y*z)/(x*y))**z
#     return w

# jawaban1 = soal1(4,3,2)
# print(jawaban1)

# # SOLVE 2
# num = input("Masukkan angka untuk dikuadratkan: ")

# def kuadratkan(num1):
#     hasil = num1**2
#     print(hasil)

# kuadratkan(int(num))

# # SOLVE 3
# import math
# jumlahHari = input("Masukkan hari untuk dijabarkan: ")

# def menjabarkanHari(jumlahHari):
#     jumlahTahun = math.floor(jumlahHari / 360)
#     sisaHari = jumlahHari - (jumlahTahun*360)
#     jumlahBulan = math.floor(sisaHari/30)
#     sisaHari2 = sisaHari - (jumlahBulan*30)
#     jumlahMinggu = math.floor(sisaHari2/7)
#     sisaHari3 = sisaHari2 - (jumlahMinggu*7)
#     jumlahHari = sisaHari3
#     print("{} tahun {} bulan {} mingggu {} hari".format(jumlahTahun, jumlahBulan, jumlahMinggu, jumlahHari))

# menjabarkanHari(int(485))

# # SOLVE 4
# a = 4/14 * 49
# b = 10/14 * 49

# usiaAndi = a + 2
# usiaBudi = b + 2

# print(int(usiaAndi))
# print(int(usiaBudi))

# # SOLVE 5
# y = "Halo Dunia".count("a")
# print(y)

# # SOLVE 6
# jamAwal = 9
# jarak = 120
# kecepatanTotal = 100/3600
# detikTotal = jarak/kecepatanTotal
# lamaJam = math.floor(detikTotal / 3600)
# lamaMenit = math.floor((detikTotal%360)/60)
# lamaDetik = math.floor((detikTotal%360)%60)
# print("Lama jam = " + str(lamaJam) + "Lama menit = " + str(lamaMenit))
# print("Tabraknya pukul " + str(jamAwal + lamaJam) + ' dan menit ke ' + str(lamaMenit) + "dan detik ke " + str(lamaDetik))


# ## SOLVE 1 BINTANG
# size = int(input("Masukkan size: "))
# z = ""

# for num in range(size):
#     for num1 in range(num, size):
#         z += " * "
#     z += "\n"

# print(z)

# # FUNGSI RETURN
# def total(x,y) : 
#     z = x + y
#     return z

# print(total(4,5))

# print(z) # Kita tidak bisa memanggil variabel lokal z

# # FUNGSI TANPA RETURN
# def total(x,y) :
#     z = x + y
#     print(z)

# print(total(4,5))

# # ACCESSING DATA IN LIST
# buah = ['Jeruk', 'Nanas', 'Apel']
# for item in buah :
#     print(item)

# # LOOKING FOR THE MODE OF A LIST
# listNum = [ 1,2,3,2,5,2,7,2]

# import statistics

# print(statistics.mode(listNum))

# # USING {}
# name = "Mike"
# print("Hello {}".format(name))

# # DATETIME NOW
# from datetime import datetime

# now = datetime.now()
# print(now)
# print(now.day)
# print(now.month)
# print(now.year)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print("{}-{}-{}".format(now.day, now.month, now.year))
# print("{}-{}-{} ".format(now.day, now.month, now.year) + "{}-{}-{}".format(now.hour, now.minute, now.second))

# # OPEN CSV OR TXT FILE
# f = open('crime_rates.csv', 'r')
# d = f.read()
# rows = d.split('\n')
# print(rows)

# # LOOPING
# cities = ["Austin", "Dallas", "Houston"]
# for city in cities:
#     print(city)

# # LOOPS
# three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]

# final_list = []

# for row in three_rows:
#     split_list = row.split(',')
#     final_list.append(split_list)

# print(final_list)

# # INDEXING
# list1 = [["titis", "123"], ["nurul", "456"]]

# numlist = []

# for line in list1:
#     name = line[0]
#     count = int(line[1])
#     newlist = [name, count]
#     numlist.append(newlist)
# print(numlist)

# # FOR
# list1 = ["a", "b", "c"]
# for item in range(1,len(list1)): 
#     print(item)

# # DICTIONARIES
# d = { "key1" : { "key2" : "item2" }, "kucing" : [3, "jerapah"] }
# print(d["key1"])
# print(d["key1"]["key2"])
# print(d["kucing"])
# print(d["kucing"][1])
# # d.append("titis") # we can't do append to dictionary
# d["key3"] = "titis" # this is how we add index and its value to dictionaries
# print(d)

# TUPLES
t = (1, [0, "test"], { "a1" : True })
# print(t[2]["a1"])
# print(t[1][1])
# t[1][1] = "akan" # we cant assign new value to tuples
# print(t[1][1])
# t[1] = "mark"; print(t[1])
# t.append("titis") # we can't do append to tuples
# print(t)

# # LIST
# a = [1,2,3]
# a.append("titis")
# print(a)

# # SETS
# s = { 1, 3, 1, 2, 2, 3 }
# print(s)
# print(list(s)[2])

list1=[1,1,2,2,3,3]
set2=set(list1)
print(set2)
