class book:
    def __init__(self):
        pass
    def nhap(self):
        self.ten = input("Nhap ten sach:")
        self.gia = int(input("Nhap gia tien:"))
        self.sotr = int(input("Nhap so trang:"))
    def xuat(self):
        print("Ten:%s\tGia tien:%d\tSo trang:%d"%(self.ten,self.gia,self.sotr))
    def out(self):
        f = open("giasach.txt","a")
        f.write("Ten:%s\tGia tien:%s\tSo trang:%s\n"%(self.ten,self.gia,self.sotr))
        f.close()
    def tb(self):
        return self.gia/self.sotr

n = int(input("Nhap so sach:"))
lt = list()
for i in range(n):
    x = book()
    x.nhap()
    lt.append(x)

for i in lt:
    i.xuat()
    

for i in range(n):
    for j in range(n):
        if lt[i].tb() > lt[j].tb():
            tg = lt[i]
            lt[i] = lt[j]
            lt[j] = tg

f = open("giasach.txt","w")
f.close()
for i in lt:
    i.xuat()
    i.out()
    



    
