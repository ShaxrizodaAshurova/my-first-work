import os
os.system("cls")

set1={'olma', 'anor', 'youtube', 'instagram', 'gilos'}
set2={'youtube', 'gilos', 'anor', 'BMW', 'Tesla', 'Nissan'}
set3={'gilos', 'olma', 'instagram', 'Tesla', 'Nissan'}

a=set1.intersection(set2)
print(f"set1 va set2 uchun umumiy bolgan mevalar: {a}")

for i in a:
    if i=='youtube' or i=='anor':
        print(i, end=" ")