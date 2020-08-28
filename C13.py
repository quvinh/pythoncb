n = int(input("Nhap n:"))
lt = list()
for i in range(n):
    x =input("Nhap ptu thu %d:"%(i+1))
    lt.append(x)

print(lt)
lt2 = set(lt)
print(", ".join(lt2))

m = 1
for i in lt2:
    if lt.count(i)>m:
        m = lt.count(i)
for i in lt2:
    if lt.count(i)==m:
        print(i," xuat hien nhieu nhat voi ",lt.count(i)," lan")
        
