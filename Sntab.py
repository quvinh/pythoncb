def snt(a):
    if a<2:
        return 0
    if a>=2:
        for i in range(2,a):
            if a%i==0:
                return 0
    return 1

x=int(input("Nhap x:"))
y=int(input("Nhap y:"))  

print("So nguyen to trong doan [",x,";",y,"]")
for i in range(x,y+1):
    d=0
    if snt(i)==1:
        d=d+1
        print(i)

if d==0:
    print("Khong co so nguyen to")