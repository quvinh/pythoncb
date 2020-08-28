hc = int(input("Nhap so:"))
lt = list()
lt2 = list()
for i in range(hc):
    lt.append([])
    for j in range(hc):
        x = int(input(" [%d][%d]: "%(i,j)))
        lt[i].append(x)

for i in range(hc):
    for j in range(hc):
        print(lt[i][j],end="  ")
    print()
    

for j in range(hc):
    lt2.append([])
    for i in range(hc):
        lt2[j].append(lt[i][j])

for i in range(hc):
    lt2[i] = sorted(lt2[i], reverse=True)#Giam dan

print("Sau khi SX theo cot:")
for j in range(hc):
    for i in range(hc):
        print(lt2[i][j],end="  ")
    print()
