def g(n):
    gt=1
    for i in range(1,n+1):
        gt*=i
    return gt

n=int(input("Nhap n:"))
s=0
while n<=0:
    n=int(input("Nhap n:"))

for i in range(1,n+1):
    s+=g(i)
print(s)