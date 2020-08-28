a=int(input("Nhap a:"))
b=int(input("Nhap b:"))
print("So hoan hao trong doan ",a," va ",b," :")
d=0
for i in range(a,b+1):
    s=0
   
    for j in range(1,i):
        if i%j==0:
            s+=j
            
    if s==i:
        print(i)
        d=d+1
if d==0:
        print("Khong co so hoan hao")
