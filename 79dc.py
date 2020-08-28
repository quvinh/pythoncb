class book:
    def __init__(self):
        pass
    def nhap(self):
        self.ten = input("Nhap ten sach:")
        self.sotr = int(input("Nhap so trang:"))
        self.gia = int(input("Nhap gia tien:"))

    def xuat(self):
        print("Ten sach:", self.ten, end="")
        print("So trang:", self.sotr, end="")
        print("Gia tien:", self.gia)


    def tk(self):
        if(self.sotr < 200 and self.gia > 100):
            self.xuat()
n = int(input("Nhap so quyen sach:"))
arr = list()
for i in range(n):
    a = book()
    a.nhap()
    arr.append(a)

for i in arr:
    i.xuat()
print("Thong ke")
for i in arr:
    i.tk()
