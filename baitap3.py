n = int(input("Nhap so phan tu:"))
lt = list()
for i in range(n):
    x = int(input("Nhap phan tu thu %d :"%(i+1)))
    lt.append(x)
s = 0
for i in lt:
    s += i

f = open("file.txt","w")
f.write(str(lt))
f.write("tong :%d"%s)
f.close()

f = open("file.txt","r")
print(f.read())
