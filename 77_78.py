
class Sach:
    def __init__(self):
        pass
    def nhap(self):
        self.ten=input("Nhap ten sach:")
        self.sotrang=int(input("Nhap so trang: "))
        self.giatien=int(input("Nhap gia tien: "))
        f=open("giasach.txt",'a')
        f.writelines(self.ten+","+str(self.sotrang)+","+ str(self.giatien))
        f.close()
    def xuat(self):
        print("Ten sach: ",self.ten)
        print("So trang: ",self.sotrang)
        print("Gia tien: ",self.giatien)
    def giatientb(self):
        return float(self.giatien/self.sotrang)
    def nhapfile(self, ten,gia,so):
        self.ten=ten
        self.giatien=gia
        self.sotrang=so
    def sosanh(self):
        f=open("ketqua.txt",'a')
        if(self.giatien>100000 and self.sotrang<200):
           f.writelines(self.ten+","+str(self.sotrang)+","+ str(self.giatien))
           f.close()


n=int(input("Nhap so luong sach: "))
arr=list()
for i in range(0,n):
   a=Sach()
   a.nhap()
   arr.append(a)

for i in arr:
    print(i.xuat())
#sap xep 77
print("=====Sap sep giam dan===== ")
for i in range(0,n):
    for j in range(i,n):
          if(arr[i].giatientb()<arr[j].giatientb()):
                   b=arr[i]
                   arr[i]=arr[j]
                   arr[j]=b
for i in arr:
    print(i.xuat())
#bai 78
print("=====sap xep tang dan=====")
for i in range(0,n):
    for j in range(i,n):
          if arr[i].giatientb()>arr[j].giatientb():
                   b=arr[i]
                   arr[i]=arr[j]
                   arr[j]=b
          if arr[i].giatientb()==arr[j].giatientb():
                   b=arr[i]
                   arr[i]=arr[j]
                   arr[j]=b
for i in arr:
    print(i.xuat())
