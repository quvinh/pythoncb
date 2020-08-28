def gt(n):
    g=1
    for i in range(1,n+1):
        g*=i
    return g

x=int(input("Nhap x:"))
ep=float(input("Nhap ep:"))

while ep>1 and ep<0:
    ep=float(input("Nhap ep:"))

i=0
s=0
while abs(x/gt(2*i+1))>ep:
    s=s+((-1)**i)*x/gt(2*i+1)
    i=i+1
print("%.2f"%s)
