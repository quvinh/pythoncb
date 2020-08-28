import math
n=int(input("Nhap n:"))
x=int(input("Nhap x:"))
s=0.00
for i in range(1,n+1):
    s=math.sqrt(x+s)
print("S= ",s)