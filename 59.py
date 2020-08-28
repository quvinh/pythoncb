h = int(input("Nhap hang:"))
c = int(input("Nhap cot:"))
lt = []

for i in range(h):
    lt.append([])
    for j in range(c):
        a = int(input("Nhap [%d][%d]:"%(i,j)))
        lt[i].append(a)

print("Matrix")
# for i in range(h):
#     for j in range(c):
#         print("%3d"%lt[i][j], end="")
#     print()
print(lt)
M = 0
vt = 0
for j in range(c):
    M += lt[0][j]

for i in range(0,h):
    m = 0
    for j in range(c):
        m += lt[i][j]  
    print("Hang %d co tong = %d"%(i+1,m))
    if m>M:
        M=m
        vt=i
print("Hang %d co tong Max = %d"%(vt+1,M))
    
    
        