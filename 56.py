h = int(input("Nhap hang:"))
c = int(input("Nhap cot:"))

lt = []
for i in range(h):
    lt.append([])
    for j in range(c):
        x = int(input("Nhap phan tu [%d][%d]:"%(i,j)))
        lt[i].append(x)

print(lt)
s = 0
ch = 0
mch = 0
for i in range(h):
    for j in range(c):
        print("%3d"%lt[i][j], end="")
        s += lt[i][j]
        if i==j:
            ch += lt[i][j]
            if lt[i][j] > mch:
                mch = lt[i][j]
    print()

print("-Tong cac ptu trong ma tran:", s)

for i in range(h):
    hang = 0
    for j in range(c):
        hang += lt[i][j]
    print("+Tong hang thu %d: %d"%(i+1,hang))

for j in range(c):
    cot = 0
    for i in range(h):
        cot += lt[i][j]
    print("+Tong cot thu %d: %d"%(j+1,cot))

print("-Tong duong cheo chinh: ",ch)
print("-Max duong cheo chin:", mch)
ma=0
for i in range(h):
    for j in range(c):
        if(ma<lt[i][j]):
            ma=lt[i][j]
print('-gia tri lon nhat cua ma tran la: %d'%ma)

for i in range(h):
    mah=0
    for j in range(c):
        if(mah<lt[i][j]):
            mah=lt[i][j]
    print('+gia tri lon nhat cua hang thu %d la: %d'%(i,mah))

for j in range(c):
    mac=0
    for i in range(h):
        if(mac<lt[i][j]):
            mac=lt[i][j]
    print('-gia tri lon nhat cua cot thu %d la: %d'%(j,mac))


mi=lt[0][0]
for i in range(h):
    for j in range(c):
        if(mi>lt[i][j]):
            mi=lt[i][j]
print('-gia tri nho nhat cua ma tran la: %d'%mi)

for i in range(h):
    mih=lt[i][0]
    for j in range(c):
        if(mih>lt[i][j]):
            mih=lt[i][j]
    print('+gia tri nho nhat cua hang thu %d la: %d'%(i,mih))

for j in range(c):
    mic=lt[0][j]
    for i in range(h):
        if(mic>lt[i][j]):
            mic=lt[i][j]
    print('+gia tri nho nhat cua cot thu %d la: %d'%(j,mic))
print("_SX hang tang:")
for i in range(h):
    print(sorted(lt[i], reverse=False))

print("_SX hang giam:")
for i in range(h):
    print(sorted(lt[i], reverse=True))

print("_SX cot giam:")
for j in range(c):
    for i in range(h-1):
        for k in range(i, h):
            if(lt[i][j] < lt[k][j]):
                tg = lt[i][j]
                lt[i][j] = lt[k][j]
                lt[k][j] = tg

for i in range(h):
    for j in range(c):
        print("%3d"%lt[i][j], end="")
    print()

ma2 = 0
for i in range(h):
    for j in range(c):
        if ma2 < lt[i][j] and lt[i][j] != ma and ma2<ma:
            ma2 = lt[i][j]
print("-Max thu2 :",ma2)
