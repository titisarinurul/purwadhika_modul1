# SOAL 1 CARA SINGKAT
newList = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16]]

def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

print(list(rotated(newList)))

# SOAL 1 CARA PANJANG
List = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]

newList = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]

inputUser = int(input("Diputar berapa kali: "))
inputUser2 = (input("Diputar ke kiri atau ke kanan? "))

if (inputUser % 4 == 0):
    newList = List
    for x in range(len(newList)):
        print(newList[x])

if (int(inputUser) % 4 == 1 and inputUser2 == "kanan"):
    newList[0][3] = List[0][0]
    newList[1][3] = List[0][1]
    newList[2][3] = List[0][2]
    newList[3][3] = List[0][3]
    newList[0][2] = List[1][0]
    newList[1][2] = List[1][1]
    newList[2][2] = List[1][2]
    newList[3][2] = List[1][3]
    newList[0][1] = List[2][0]
    newList[1][1] = List[2][1]
    newList[2][1] = List[2][2]
    newList[3][1] = List[2][3]
    newList[0][0] = List[3][0]
    newList[1][0] = List[3][1]
    newList[2][0] = List[3][2]
    newList[3][0] = List[3][3]
    # for i, j in zip(range(4), range(3,-1,-1)):
    #     listHasil[0][i] = list1[j][0]
    for x in range(len(newList)):
        print(newList[x])

if (int(inputUser) % 4 == 1 and inputUser2 == "kiri"):
    newList[3][0] = List[0][0]
    newList[2][0] = List[0][1]
    newList[1][0] = List[0][2]
    newList[0][0] = List[0][3]
    newList[3][1] = List[1][0]
    newList[2][1] = List[1][1]
    newList[1][1] = List[1][2]
    newList[0][1] = List[1][3]
    newList[3][2] = List[2][0]
    newList[2][2] = List[2][1]
    newList[1][2] = List[2][2]
    newList[0][2] = List[2][3]
    newList[3][3] = List[3][0]
    newList[2][3] = List[3][1]
    newList[1][3] = List[3][2]
    newList[0][3] = List[3][3]
    for x in range(len(newList)):
        print(newList[x])

if (int(inputUser) % 4 == 2):
    newList[3][3] = List[0][0]
    for x in range(len(newList)):
        print(newList[x])