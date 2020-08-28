h = int(input("Nhap hang:"))
c = int(input("Nhap cot:"))

lt = list()
for i in range(h):
    lt.append([])
    for j in range(c):
        x = int(input("Nhap ptu[%d][%d]:"%(i,j)))
        lt[i].append(x)

m = 0
for i in range(h):
    for j in range(c):
        print(lt[i][j],end="  ")
        if lt[i][j]>m:
            m = lt[i][j]
    print()
n = lt[0][0]
for i in range(h):
    for j in range(c):
        if lt[i][j]<n:
            n = lt[i][j]

print("Max:",m)
print("Min:",n)
