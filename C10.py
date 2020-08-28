def shh(n):
    x = 0
    for i in range(1,n+1):
        if n%i==0:
            x += i
    if x==2*n:
        return 1
    return 0

n = int(input("Nhap so:"))
if shh(n)==1:
    print("%d la so hoan hao"%n)
else:
    print("%d ko la so hoan hao"%n)
