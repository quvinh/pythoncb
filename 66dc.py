b = input("Nhap day nhi phan:")
lt = b.split(",")
lt2 = []
for i in lt:
    # print(int(i,2),end=",")
    lt2.append(str(int(i,2)))
print(", ".join(lt2))