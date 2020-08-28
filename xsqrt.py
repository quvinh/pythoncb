import math
x=int(input("nhap x:"))
n=int(input("nhap n:"))
s=0
for i in range(1,n+1):
    s=math.sqrt(x+s)

print("S= %.2f"%(s+1))
    