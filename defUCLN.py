def ucln(a,b):
    while a!=b:
        if a>b:
            a=a-b
        if a<b:
            b=b-a
    return a
#a=int(input("Nhap a:"))
#b=int(input("Nhap b:"))
#print(ucln(a,b))
