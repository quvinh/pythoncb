def gt(n):
    g = 1
    for i in range(1,n+1):
        g *= i
    return g

ep = float(input("Nhap ep:"))
while ep<=0 or ep>=1:
    ep = float(input("Nhap ep:"))
x = int(input("Nhap x:"))

s = 1
i = 1
while ep < abs(x**i/gt(i)):
    s += x**i/gt(i)
    i += 1

print("e^x = %.2f"%s)
