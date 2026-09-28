set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

a=set1.symmetric_difference(set2)
for i in sorted(a, reverse=True):
    print(i, end=" ")
    