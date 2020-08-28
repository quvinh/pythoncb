def ucln(a,b):
    while(a!=b):
        if a>b:
            a = a-b
        if b>a:
            b = b-a
    return a

def bcnn(a,b):
    return a*b/ucln(a,b)

x = int(input("Nhap so thu 1:"))
y = int(input("Nhap so thu 2:"))
print("UCLN: %d\nBCNN: %d"%(ucln(x,y),bcnn(x,y)))
