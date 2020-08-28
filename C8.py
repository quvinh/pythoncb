def nt(n):
    if n == 1:
        return 0
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return 0
    return 1

n = int(input("Nhap so:"))
if nt(n)==1:
    print("%d la so nguyen to"%n)
else:
    print("%d ko la so nguyen to"%n)
