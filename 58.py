h = int(input("Nhap hàng:"))
c = int(input("Nhap cột:"))

lt = []
for i in range(h):
    lt.append([])
    for j in range(c):
        x = int(input("Nhập vị trí [%d][%d]:"%(i,j)))
        lt[i].append(x)


print(lt)
for i in range(h):
    s=0
    for j in range(c+1):
        if j<c:
            s += lt[i][j]
            print(lt[i][j], end=" ")
        if j==c:
            print(s)
    print()
