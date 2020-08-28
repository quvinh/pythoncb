h = int(input("Nhap hang:"))
c = int(input("Nhap cot:"))
lt = list()

for i in range(h):
    lt.append([])
    for j in range(c):
        x = float(input("Nhap pt[%d][%d]:"%(i,j)))
        lt[i].append(x)

for i in range(h):
    s=0
    for j in range(c):
        print(lt[i][j], end="\t")
        s += lt[i][j]
        
    print(s)
    print()

for i in range(h):
    mh = 0
    for j in range(c):
        mh += lt[0][j]
    break

for i in range(h):
    t = 0
    for j in range(c):
        t += lt[i][j]
    if t>mh:
        mh = t
    print("Tong hang %d : %.2f"%(i+1,t))

print("Max hang:",mh)
    


