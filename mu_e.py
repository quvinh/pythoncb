import math
x=int(input("Nhap x:"))
ep=float(input("Nhap ep:"))

def gt(a):
    g=1
    for i in range(1,a+1):
        g=g*i
    return g


s=0.0
i=1
while(abs(x**i/gt(i))>ep):
    s+=float(x**i/gt(i))
    i=i+1
print(s+1)