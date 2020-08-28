#25
def gt(n):
    g=1
    if n==0:
        return 1
    else:
        for i in range(1,n+1):
            g *= i
        return g

n = int(input("Nhap n:"))
x = int(input("Nhap x:"))
s = 0
for i in range(n):
    s += x/gt(2*i +1)

print("S = %.2f"%s)
