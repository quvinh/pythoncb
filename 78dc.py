from operator import*
class book:
    def __init__(self, tens, sotr, tien):
        self.tens = tens
        self.sotr = sotr
        self.tien = tien
    def __str__(self):
        return ("Ten sach:%s  So trang:%d  Giatien:%d"%( self.tens, self.sotr, self.tien))
    
b = []
b2 = []
n = int(input("Nhap so quyen sach:"))
for i in range(n):
    print("-Quyen sach thu %d:"%(i+1))
    a1 = input("Nhap ten sach:")
    a2 = int(input("Nhap so trang:"))
    a3 = int(input("Nhap gia tien:"))
    x = book(a1, a2, a3)
    print(x)
    y = (a1,a2,a3)
    b.append(x)
    b2.append(y)


s = sorted(b2, key = itemgetter(2), reverse = False)
print(s)
f = open("file.txt", "a")
f.write(str(s))
f.close()