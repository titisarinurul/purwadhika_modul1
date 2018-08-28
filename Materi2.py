# #MATERI HARI KEDUA

# x = "Halo Dunia Hello"

# print(len(x))
# print(x.index("Dun"))
# hasilSplit = x.split()
# print(hasilSplit)
# print(x.lower())
# print(x.upper())
# print(x.capitalize())
# print(hasilSplit[])

# # kalau mau bikin array yg hanya terdiri dari "halo" dan "hello"
# output = []
# output.append(hasilSplit[0])
# output.append(hasilSplit[2])
# print(output)

# print(x[1])
# print(x[5:]) #kita nentuin awal tp g nentuin batas akhir
# print(x[:6]) #kita g nentuin awal tp nentuin batas akhir
# print(x[3:6])

# usia = 25
# nama = "Baron"
# print(nama + ' usianya ' + str(usia)) # usia diubah ke string dulu


# if(False == False):
#     print("Hello") # krn kondisi di if Trues, maka akan menjalankan fungsi di dalam if

# if(True):
#     print("Hello")
# elif(True):
#     print("Apa kabar?")

# SOAL 1
# angka = int(input("Masukkan angka : "))

# if(angka%2/=0):
#     print("angka " + str(angka) + "tergolong bilangan GANJIL!)
# elif(int(angka)%2==0):
#     print("angka " + str(angka) + "tergolong bilangan GENAP!")

# angka = input("Masukkan angka : ")
# jenis = "GANJIL!";
# if(int(angka)%2==0):
#     jenis = "GENAP!";
# print("Angka " + angka + " tergolong bilangan " + jenis);

# SOAL 2
massa = int(input("Masukkan massa(kg): "))
tinggi = int(input("Masukkan tinggi(cm): "))
IMT = massa / ((tinggi/100)**2)

text = ""

if (IMT < 18.5):
    text = "BERAT BADAN KURANG!"
elif(IMT >= 18.5 and IMT <= 24.9):
    text = "BERAT BADAN IDEAL!"
elif(IMT >= 25 and IMT <= 29.9):
    text = "BERAT BADAN BERLEBIH!"
elif(IMT >= 30 and IMT <= 39.9):
    text = "BERAT BADAN SANGAT BERLEBIH!"
else:
    text = "OBESITAS!"

print("Massa " + str(massa) + " kg & tinggi " + str(tinggi/100) + " m")
print("IMT = " + str(IMT) + ", " + text)