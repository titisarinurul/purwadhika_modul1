# 1
angka = 1

while(angka<=10):
    print(angka)
    angka +=1

# 2
listItem = list(range(1,11,2)) #(mulai dari apa, berhenti dimana, kelipatannya brp)
print(listItem)

for item in range(1,11,2): 
    print(item) # dia akan ngeprint satu2

# 3
for item in range (1,11,1): # bs jg ditulis (1,11) krn otomatis dianggap kelipatan 1
    print("Nomor urut " + str(item))

# 4
for item in range (0,21,2):
    print("Nomor urut " + str(item))

# 5
for item in range (1,20,2):
    print("Nomor urut " + str(item))

# 6
listTipe = ["Sans", 50, "Biasa", True] # bs terdiri lbh dari 1 tipe data
for tipe in listTipe:
    print(tipe) 

# 7 for loop drawing
z=''
for item in range(0,5): # ini mubazir krn ud pasti mulai dari 0
    z += ' * '
print(z)

# 8 again. for loop drawing
z=''
for item in range(0,5): 
    z += ' * \n'
print(z)

# 9 loop drawing again
z = ''
for item in range(0,5):
    for item1 in range(0,5):
        z += ' * '
    z += '\n'
print(z)

# 10 still loop drawing
z = ''
for item in range(0,5):
    for item1 in range (0,item+1):
        z += ' * '
    z += '\n'
print(z)

# 11 still loop drawing
angka = int(input("Masukkan angka : "))

z = ''
for item in range(0,angka):
    for angka in range (0,int(angka)):
        z += ' * '
    z += '\n'
print(z)

# 12 still not solved!
angka = int(input("Masukkan angka : "))
z = ''

for item in range (int(angka), 0, -1):
    for item1 in range (0,item):
         z += ' * '
         if (' * ' == 1):
            for item2 in range (0,item):
                z += ' * '
    z += '\n'
print(z)

# 13
n = int(input("Masukkan angka : "))

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

for i in range(2,(n+1)):
    for j in range(i):
        print ('* ', end="")
    print('')

# 14
k= int(input("Masukkan angka : "))

for i in range (0,k):
    for j in range(0,k-1-i):
        print("* ", end="")
    for z in range (0,i+1):
        print("# ", end="")
    print("\r")

# # 15
k= int(input("Masukkan angka : "))

for i in range (0,k):
    for j in range (0,i):
        print ("# ", end= "")
    for z in range (0,k-1):
        print ("* ", end="")
    print("\r")


# solve 1
size =
z = ""

for num in range (size):
    for num1 in range (num, size):
        z += " * "
    z += "\n"

print(z)

# solve 2
