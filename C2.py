def gt(n):
    g=1
    for i in range(1,n+1):
        g*=i
    return g

a = float(input("Nhap a:"))
while a<0 or a>0.01:
    a = float(input("Nhap a:"))

i = 0
s = 0
while a < 1/(2*i+1):
    s += 1/gt(2*i+1)
    i += 1

print("S = %.3f"%s)
