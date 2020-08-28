def snt(a):
    if(a<2):
        return 0
    if(a>=2):
        for i in range(2,a):
            if a%i==0:
                return 0
    return 1

print("SNT trong n->m:")
n=int(input("Nhap n:"))
m=int(input("Nhap m:"))

while n>=m:
    print("Nhap lai! n->m:")
    n=int(input("Nhap n:"))
    m=int(input("Nhap m:"))

print("So nyen to trong [%d,%d]:"%(n,m))
d=0
for i in range(n,m+1):
    
    if snt(i) == 1:
        d=d+1
        print(i,end=" ")

if d==0:
    print("Khong co !")
        
