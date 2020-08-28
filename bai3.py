n=int(input("Nhap n:"))
s=0
d=0
for i in range (1,n+1):
    if n%i==0:
        s+=i
        d=d+1
print("TBC cac uoc:",(1.0*s)/d)