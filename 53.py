n = int(input("Nhap bn so:"))
lt = []
for i in range(n):
    x = input("Nhap so thu %d:"%(i+1))
    lt.append(x)

print("_Dãy vừa nhâp:")
print("; ".join(lt))

def nt(a):
    if a < 2: return 0
    else:
        for i in range(2, a):
            if a%i == 0:
                return 0
    return 1
lt2 = []
for i in range(n):
    if nt(int(lt[i]))==1:
        lt2.append(lt[i])

s = set(lt2)
print("_Các số nguyên tố:")
print("; ".join(s))