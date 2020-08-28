n=int(input("Nhap n:"))
m=int(input("Nhap m:"))

a=[]
for i in range(m):
    a.append([])
    for j in range(n):
        x=int(input("Nhap pt thu a[%d][%d]:"%(i+1,j+1)))
        a[i].append(x)

print("Day so :")
for i in range(m):
    for j in range(n):
        print("%3d"%a[i][j],end="")
    print()
