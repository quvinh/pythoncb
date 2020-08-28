class sv:
    def __init__(self):
        pass
    def nhap(self):
        self.ten = input("Nhap ten sv:")
        self.masv = int(input("Nhap ma sv:"))
        self.diem = float(input("Nhap diem sv:"))
        f = open("doc.txt","a")
        f.writelines("Ten:%s Masv:%d Diem:%.2f"%(self.ten, self.masv, self.diem))
        f.writelines("\n")
        f.close()   
    def xuat(self):
        print("Ten:%s Masv:%d Diem:%.2f"%(self.ten, self.masv, self.diem))
    
    def getdiem(self):
        return self.diem
    

n = int(input("Nhap so SV:"))
lt = list()
for i in range(n):
    s = sv()
    s.nhap()
    lt.append(s)

# for i in lt:
#     i.xuat()
print("Doc file:")
f = open("doc.txt","r")
print(f.read())
f.close()

m = 0
for i in lt:
    if i.getdiem() > m:
        m = i.getdiem()

print("SV co diem cao nhat:")
for i in lt:
    if m == i.getdiem():
        i.xuat()

