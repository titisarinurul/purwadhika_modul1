print('hello')
nama = 'Andi'
print(nama)

usia = 22
usia = 32
print(usia)

jomblo = True
print(jomblo)
print(type(nama))
print(type(usia))
print(type(jomblo))

# nama = input('whats your name? :')
# print(nama)

nama = input("Nama kamu? : ")
umur = input ("Umur kamu? : ")
kelamin = input("Kelamin kamu? :")
pekerjaan = input("Pekerjaan kamu? :")

print ("Nama: " + nama)
print("Umur: " + umur)
print("Kelamin : " + kelamin)
print("Pekerjaan :" + pekerjaan)


#CONTOH 1
def test(angka1):
    hasil1 = angka1 + angka1
    return hasil #hasilnya 10

def mumet(angka1):
    hasil = angka1 + angka1 #hasilnya akan none

num1 = 5
jawaban = test(num1) #pengetesan def test dan mumet
print(jawaban) 

# CONTOH 2
def mumet1(angka2):
    hasil = angka2 + angka2
    print(hasil)
mumet1(12)


# CONTOH 3
def mumet2(angka2):
    hasil3 = angka2 + angka2
    print(hasil3)
    return 1000

ab = mumet2(10)
print(ab)