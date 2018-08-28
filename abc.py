
# # SOAL 1
# for angka in range(1,21,1): 
#     if (angka % 15 == 0) :
#         print ("fizzbuzz")
#     elif (angka % 3 == 0) :
#         print ("fizz")
#     elif (angka % 5 == 0 ) :
#         print ("buzz")
#     else :
#         print(angka)

# # SOAL 2

# def fibo(urut) : 
#     listData = [1,1]; 
#     for i in range(2,urut): 
#         listData.append(listData[i-2] + listData[i-1]); 
#     # return listData[urut-1]; # agar bisa diakses atau dipanggil diluar
#     return listData

# print(fibo(8));

# # SOAL 3

# # Cara g bener
# x = [1,2,3,4,5,6,7,8]

# def reverseList(list1):
#     for i in range(len(list1)):
#         for j in range (i+1, len(list1)):
#             if list1[i] < list1[j]:
#                 list1[i], list1[j] = list1[j], list1[i]
#     print(list1)

# # Cara bener
# import math
# def reverseList(theList) : 
#     for i in range(0, math.floor(len(theList)/2)) : 
#         tempList = theList[i]; 
#         theList[i] = theList[len(theList) - 1 - i]; 
#         theList[len(theList) - 1 - i] = tempList;
# return theList;
# print(reverseList([1,2,3,4,5,6,7,8]));

# reverseList(x)

# # Bubble short: dr belakang ke depan, i jd batas akhir
# # selection short: dr depan ke belakang

# # SOAL 4

# theList = [1,2,3,2,5,2,7,2]

# def mean(thelist):
#     mean = sum(thelist)/len(thelist)
#     print(mean)

# mean(theList)

# def median(list1):
#     for i in range(len(list1)):
#         for j in range (i+1, len(list1)):
#             if list1[i] > list1[j]:
#                 list1[i], list1[j] = list1[j], list1[i]
#     print(list1)
#     print((list1[3]+list1[4])/2)

# median(theList)
