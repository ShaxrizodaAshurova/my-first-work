a=input("1-so'zni kiriting: ")
b=input("2-so'zni kiriting: ")
sorted(a)
sorted(b)
if len(a)==len(b):
    if sorted(a)==sorted(b):
        print(True)
    else:
        print(False)