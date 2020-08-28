h = int(input("Nhap hang:"))
c = int(input("Nhap cot:"))

a = []
for i in range(h):
    a.append([])
    for j in range(c):
        x = int(input("Nhap phan tu thu [%d][%d]:"%(i,j)))
        a[i].append(x)


f = open("file.txt","w")
for i in range(h):
    for j in range(c):
        f.writelines(str(a[i][j]))
        f.writelines("\t")
    f.writelines("\n")
f.close()

print("Doc file lan 1:")
f = open("file.txt","r")
print(f.read())
f.close()

f = open("file.txt","w")
for i in range(h):
    m = 0
    for j in range(c):
        if m <= a[i][j]:
            m = a[i][j]
        f.writelines(str(a[i][j]))
        f.writelines("\t")
    f.writelines(str(m))
    f.writelines("\n")
    
for j in range(c):
    s=0
    for i in range(h):
        s += a[i][j]
    f.writelines(str(s))
    f.writelines("\t")
f.close()

print("Doc file lan 2:")
f = open("file.txt","r")
print(f.read())
f.close()
