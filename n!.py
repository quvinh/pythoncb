def zaithua(n):
    gt=1
    for i in range(1,n+1):
        gt*=i
    return gt

n=int(input("Nhap n:"))
while n<=0:
    n=int(input("Nhap n:"))

print(n,"!= ",zaithua(n))
