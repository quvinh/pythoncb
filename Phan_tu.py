
n=int(input("Nhap so phan tu: "))

lt=[]
for i in range(0,n):
    lt.append(str(input("_Nhap phan tu thu %d :"%i)))

print("Mang vua nhap:",end=" ")
print(", ".join(lt))

a=int(input("Nhap so a: "))
b=int(input("Nhap so b: "))

for i in range(a,b+1):
    print(lt[i])

s=0
c=0
for i in range(0, n):
    s+=int(lt[i])
    c+=1
print("Tong cac ptu: ",s)
print("TBC cac ptu: %.2f"%(s/c))

print("_Max = ",max(lt))
print("_Min = ",min(lt))

lt.sort()
print(end="Sap xep mang tang dan: ")
print(", ".join(lt))

lt.sort(reverse=True)
print(end="Sap xep mang giam dan: ")
print(", ".join(lt))

x=input("Nhap ptu b:")
print("=> ",x," xuat hien ",lt.count(x), "lan")
for i in range(n):
    if x==lt[i]:
        print("_o vi tri :",i)

o=int(input("Nhap so: "))
m=int(input("Nhap so: "))

for i in range(n):
    if int(lt[i])>=o and int(lt[i])<=m :
        print(lt[i])

for i in range(n):
    if(int(lt[i])>0):
        print("-Gia tri phan tu duong dau tien :",lt[i],"/vi tri: ",i)
        break
vt=0
for i in range(n):
    if(int(lt[i])>0):
        vt=i
print("-Gia tri phan tu duong cuoi cung :",lt[vt],"/vi tri: ",vt)

i1=int(input("Nhap vi tri can chen: "))
i2=input("Nhap gia tri can chen: ")        
lt.insert(i1,i2)
print(lt)

r=input("Nhap gia tri can xoa: ") 
lt.remove(r)
print(lt) 

l=set(lt)
print("Cac so khac nhau: ",l)

for i in range(n):
    print("Tan suat xuat hien ptu ",lt[i]," = ",lt.count(lt[i]))


ts=[lt.count(i) for i in lt]
for i in range(len(lt)):
    if ts[i]==max(ts):
        print("So xuat hien nhieu nhat: ",lt[i])
        print("Xuat hien: ",max(ts)," lan")
        break

g=dict()
for i in range(len(lt)):
    g[lt[i]]=ts[i]
print("Tan suat cac so: ",g)