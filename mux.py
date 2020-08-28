n=int(input("Nhap n:"))
x=int(input("Nhap x:"))
s=0
for i in range(1,n+1):
    s+=x**i
print("S = ",s)