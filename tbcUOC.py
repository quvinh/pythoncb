n=int(input("Nhap n:"))
d=0
s=0
for i in range(1,n+1):
    if n%i==0:
        s+=i
        d=d+1

print("TBC uoc :",float(s/d))
