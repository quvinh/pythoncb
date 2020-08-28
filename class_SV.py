class SV:
    def __init__(self, ten, masv, diachi):
        self.ten = ten
        self.masv = masv
        self.diachi = diachi
    
    def __str__(self):
        return ("Ten sv: %s  Masv: %d  Diachi: %s"%(self.ten,self.masv,self.diachi))
    
n = int(input("Nhap so sinh vien:"))
lt = []
for i in range(n):
    sv = SV(input("Nhap ten sv:"), int(input("Nhap masv:")), input("Nhap diachi:"))
    lt.append(sv)
    print(sv)



