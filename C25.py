hc = int(input("Nhap so:"))
lt = list()
for i in range(hc):
    lt.append([])
    for j in range(hc):
        x = int(input(" [%d][%d]: "%(i,j)))
        lt[i].append(x)

for i in range(hc):
    for j in range(hc):
        print(lt[i][j], end="  ")
    print()

for i in range(hc):
    lt[i] = sorted(lt[i])#Tang dan
print("SX theo hang:")
for i in range(hc):
    for j in range(hc):
        print(lt[i][j], end="  ")
    print()
