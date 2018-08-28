# # PERCOBAAN 1 MASIH SALAH
# def MainMenu() :
#     inputUser = input("Main Menu : \n 1. Pilih Angka\n 2. Lihat List Angka\n 3. Lihat Score Board\n 4. Keluar\n\n Pilih Menu : ");
#     return inputUser;

# def pilihAngka(inputAngka) :
#     print("Pilihan Angka : ");
#     for i in range(len(inputAngka)) :
#         print(inputAngka[i]);
#     inputUser = input("Mau angka yang mana? : ");
#     return [int(inputUser)]

# def lihatList(inputAngka):
#     print("Ini List Angka : ");
#     for i in range(len(inputAngka)) :
#         print(inputAngka[i]);

# def scoreBoard(inputAngka):
#     print("Score board kita : ")
#     for i in range(len(inputAngka)):
#         if (i == 1):
#             print("benar")
#         else:
#             print ("try again")

# daftarAngka = [1,2,3]
# inputAngka = []

# while True:
#     check = MainMenu();
#     if(check == "1") :
#         inputAngka.append(pilihAngka(daftarAngka));
#     elif(check == "2") :
#         lihatList(inputAngka);
#     elif(check == "3"):
#         scoreBoard(inputAngka)
#     elif(check == "4"):
#         print("Bye!")
#         break


# PERCOBAAN 2 JAWABAN BENAR
lib_lampu={
    '1':[0,1,0,1,0],
    '2':[1,1,1,2,1],
    '3':[1,1,1,1,1],
    '4':[0,3,1,1,0],
    '5':[1,2,1,1,1],
    '6':[1,2,1,3,1],
    '7':[1,1,0,1,0],
    '8':[1,3,1,3,1],
    '9':[1,3,1,1,1]
}

def MainMenu() :
    inputUser = input("Main Menu : \n 1. Input List\n 2. Lihat List\n 3. Keluar\n\n Pilih Menu : ");
    return inputUser;

def lihatList(inputAngka):
    temp=''
    for i in range(0,5):
        for angka in inputAngka:
            if i%2==0:
                if lib_lampu[angka][i]==0 : temp+='     '
                elif lib_lampu[angka][i]==1 : temp+=' === '
            else:
                if lib_lampu[angka][i]==0 :   temp+='     '
                elif lib_lampu[angka][i]==1 : temp+='    |'
                elif lib_lampu[angka][i]==2 : temp+='|    '
                elif lib_lampu[angka][i]==3 : temp+='|   |'
            temp+='   '
        temp+='\n'
    print(temp)    
    print(inputAngka)

inputAngka = []
while True:
    check = MainMenu();
    if(check == "1") :
        inputAngka.append(input('Masukkan Angka(1-9): '))
    elif(check == "2") :
        lihatList(inputAngka);
    elif(check == "3"):
        print("Bye!")
        break