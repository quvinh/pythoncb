n = int(input("Nhap n:"))
lt = list()

for i in range(n):
    lt.append([])
    for j in range(n):
        x = int(input("Nhap [%d][%d]:"%(i,j)))
        lt[i].append(x)

f = open("file.txt","w")
for i in range(n):
    for j in range(n):
        f.writelines(str(lt[i][j]))
        f.writelines(" ")
    f.writelines("\n")
f.close()
