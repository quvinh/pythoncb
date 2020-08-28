pt = int(input("Nhap so phan tu:"))
lt = []
for i in range(pt):
    lt.append(input("_Nhap phan tu thu %d: "%i))

print("Mang vua nhap:")
print(", ".join(lt))
lt2 = set(lt)
for i in lt2:
    print(i,"xuat hien ",lt.count(i)," lan.")