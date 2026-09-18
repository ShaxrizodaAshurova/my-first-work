# 1. juft a dan b gacha bolgan hamma  juft sonlarni bitta list ichiga joylashtirish

# a=int(input("a:"))
# b=int(input("b:"))
# lst=[]
# for i in range(a, b):
#     if i%2==0:
#         print (i, end=" ")

# =================================================================

# 2.Tuple e'lon qilingan va ushbu tuplening boshidagi 4-elementni va oxiridan 4-elementni chiqarish

# t=(1,2,3,4,5,6,7,8,9,10)
# print(t[3], t[-4])

# =================================================================

# 3. List ichida tuplelar berilgan va ushbu tuplelarning oxirgi elementini 100 bilan almashtirish

# lst=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# lst[2]=(70,80,100)
# print(lst)


# =================================================================


# 4.Input orqali kiritilgan string ma'lumotlarni tuplega bittalab(har bir belgisini) joylashtirish
 
# n=input("matn kiriting: ")
# tple=()
# for i in n:
#     tple+=(i,) 
# print(tple)

# ==================================================================


# 5.Sonlardan iborat listlarni o'zida saqlaydigan list berilgan. Ichki listlarning elementlar yig'indisi eng katta bo'lgan listni topish

# lst=[ [1,2,3], [4,5,6], [10,11,12], [7,8,9] ]
# max_sum=0
# max_lst=0
# for i in lst:
#     sum=0
#     for j in i:
#         sum+=j
#     if sum>max_sum:
#         max_sum=sum
#         max_lst=i

       
# print(max_sum)
# print(max_lst)

# =====================================================================

# 6.List va String ma'lumotlarini berilgan. Listdagi barcha elementlarning boshiga berilgan stringni qo'shib qo'yish

lst = [1,2,3,4]
string = "emp"

yangi = []

for i in lst:
yangi.append(string + str(i))

print(yangi)    




  


