import os
os.system("cls")


set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
natija=set1.intersection(set2)
faqat1=set1.difference(set2)

yigindi=0

for i in natija:
    yigindi+=i
    
print(f"umumiy yigindi: {yigindi}")
print(faqat1)


yigindi2=0
for i in faqat1:
    yigindi2+=i
print(yigindi-yigindi2)


