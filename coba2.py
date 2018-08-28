namaPaket1 = "Paket Hoki A"
namaPaket2 = "Paket Hoki B"
namaPaket3 = "Paket Hoki C"
hargaPaket1 = int(20000)
hargaPaket2 = int(15000)
hargaPaket3 = int(30000)

print("Selamat datang di Hoki-hoki Bento!")

def mainMenu():
    print ("Main Menu")
    print ("1. Lihat Menu \n2. Lihat Cart \n3. Checkout \n4. Keluar")

mainMenu()

pilihan = int(input("Masukkan pilihan main menu : "))

if (pilihan > 0 and pilihan < 5):
    if (pilihan == 1):
        print(f"Menu: \n1. {namaPaket1} Rp {hargaPaket1} \n2. {namaPaket2} Rp {hargaPaket2} \n3. {namaPaket3} Rp {hargaPaket3} \n4. Sudah selesai memesan")
    if (pilihan == 2):
        print("Cart anda: ")
    if (pilihan == 3):
        print("Check out: ")
    if (pilihan == 4):
        print("Anda sudah keluar. Sampai berjumpa lagi!")

# sudah masuk halaman menu dan mau memilih menu makanan
angka = int(input("Masukkan pilihan menu : "))
listMakanan = ""
tHarga = 0

while (angka >=0):
    if (angka == 1):
        listMakanan += namaPaket1
        tHarga += hargaPaket1
        print (f"Anda sudah memesan {listMakanan} dengan harga Rp {tHarga}")
        
        mainMenu()
        break
    elif (angka == 2):
        listMakanan += namaPaket2
        tHarga += hargaPaket2
        break 
    elif (angka == 3):
        listMakanan += namaPaket3
        tHarga += hargaPaket3
        break
    elif (angka == 4):
        print (f"Pesanan anda: {listMakanan}, Rp {tHarga}")
        break 

# masuk ke halaman cart
# print ("Cart:")
# print (f"{listMakanan}, Rp {tHarga}")

# masuk ke halaman check out
# print ("Check Out")
# print (listMakanan)
# print (tHarga)