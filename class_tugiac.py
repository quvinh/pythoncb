import math
class hinh:
    def __init__(self, a = 0, b = 0, c = 0, d = 0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

class hcn(hinh):
    def __init__(self):
        hinh.__init__(self)
        print("Hinh chu nhat")
    def nhap(self):
        self.a = int(input("Nhap canh 1:"))
        self.b = int(input("Nhap canh 2:"))
    def dt(self):
        return self.a * self.b

class hv(hinh):
    def __init__(self):
        hinh.__init__(self)
        print("Hinh vuong")
    def nhap(self):
        self.a = int(input("Nhap canh :"))
    def dt(self):
        return self.a * self.a

class thang(hinh):
    def __init__(self):
        hinh.__init__(self)
        print("Hinh thang")
    def nhap(self):
        self.a = float(input("Nhap canh day 1:"))
        self.b = float(input("Nhap canh day 2:"))
        self.c = float(input("Nhap chieu cao:"))
    
    def tt(self):
        # d1 = i for i in range(self.b/2)
        d1 = 1
        d2 = self.b - d1
        c1 = math.sqrt(d1**2 + (self.c)**2)
        c2 = math.sqrt(d2**2 + (self.c)**2)
        print("Day lon: %.2f, Day nho: %.2f, Chieu cao: %.2f, Canh ben: %.2f, Canh ben 2: %.2f"%(self.b,self.a, self.c, c1, c2))
    def dt(self):
        return ((self.a + self.b)*self.c)/2

# cn = hcn()
# cn.nhap()
# print("S = ", cn.dt())

# v = hv()
# v.nhap()
# print("S = ", v.dt())

arr = list()
n = int(input("Nhap so hinh:"))
for i in range(n):
    t = thang()
    t.nhap()
    arr.append(t)
print("Hien thi")
for i in arr:
    print("S = ", i.dt())
    i.tt()

