set1={4,5,6,7,8,9}
set2={5,6,7,10,11}
set3=set1.intersection(set2)
set4=set1.symmetric_difference(set2)
set5=sum(set4)-sum(set3)
print(set5)