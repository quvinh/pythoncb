class book:
    def __init__(self):
        pass
    def nhap(self):
        self.ten = input("Nhap ten:")
        self.sotr = int(input("Nhap so trang:"))
        self.gia = int(input("Nhap gia tien:"))
    def xuat(self):
        print("Ten sach:%s\tGia tien:%d\tSo trang:%d"%(self.ten,self.gia,self.sotr))
    def giaTB(self):
        return self.gia/self.sotr
    def xf(self):
        f = open("giasach.txt","a")
        f.write("\nTen sach:%s\tGia tien:%s\tSo trang:%s"%(self.ten,self.gia,self.sotr))
        f.close()

n = int(input("Nhap n sach:"))
lt = list()
for i in range(n):
    a=book()
    a.nhap()
    lt.append(a)

for i in lt:
    i.xuat()

for i in range(n):
    for j in range(i,n):
        if lt[i].giaTB() > lt[j].giaTB():
            tg = lt[i]
            lt[i] = lt[j]
            lt[j] = tg
f = open("giasach.txt","w")
f.close()
for i in lt:
    i.xuat()
    i.xf()


