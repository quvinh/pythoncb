n = int(input("Nhap n so:"))
lt = list()
for i in range(n):
    x=int(input("Nhap pt thu %d :"%(i+1)))
    lt.append(x)

print(lt)

a = int(input("Nhap a:"))
b = int(input("Nhap b:"))
while a>b:
    a = int(input("Nhap a:"))
    b = int(input("Nhap b:"))

for i in range(n):
    if lt[i]>=a and lt[i]<=b:
        print(lt[i], end=" ")

