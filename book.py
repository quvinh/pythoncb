class book:
    def __init__(self):
        pass
    def nhap(self):
        self.ten = input("Nhap ten:")
        self.sotrang = int(input("Nhap so trang:"))
        self.giatien = int(input("Nhap gia tien:"))
    def xuat(self):
        print("Ten sach:",self.ten)
        print("So trang:",self.sotrang)
        print("Gia tien:",self.giatien)

    def giaTB(self):
        return float(self.giatien/self.sotrang)


n = int(input("Nhap so luong sach:"))
arr = []
for i in range(n):
    a=book()
    a.nhap()
    arr.append(a)

for i in arr:
    print(i.xuat())

print("=====Sap sep giam dan===== ")
for i in range(0,n):
    for j in range(i,n):
          if(arr[i].giaTB()<arr[j].giaTB()):
                   b=arr[i]
                   arr[i]=arr[j]
                   arr[j]=b
for i in arr:
    print(i.xuat())
