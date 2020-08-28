a=[]
h=int(input("Nhap hang:"))
c=int(input("Nhap cot:"))

for i in range(h):
    a.append([])
    for j in range(c):
        x=int(input("Nhap phan tu thu a[%d][%d] :"%(i,j)))
        a[i].append(x)

print("Mang vua nhap la:")
# for i in range(h):
#     for j in range(c):
#         print("%3d"%a[i][j], end=" ")
#     print()

for i in a:
    print(i)