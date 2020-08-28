h = int(input("Nhap hang: "))
c = int(input("Nhap cot: "))
a=[]

for i in range(h):
    a.append([])
    for j in range(c):
        a[i].append(i*j)

for i in range(h):
    for j in range(c):
        print("%3d"%a[i][j], end="")
    print()