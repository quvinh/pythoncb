import math
class hinh:
    def __init__(self, socanh=0):
        self.n = socanh
        self.canh = [0 for i in range(socanh)]
    def nhap(self):
        self.canh = [float(input("Nhap canh thu %d :"%(i+1))) for i in range(self.n)]
    def incanh(self):
        for i in range(self.n):
            print("Gia tri canh ", i+1, " la:", self.canh[i])
        

class hv(hinh):

    def __init__(self):
        hinh.__init__(self, 1)
        print("Hinh vuong")
    def dt(self):
        a = self.canh[0]
        return a*a

class hcn(hinh):

    def __init__(self):
        hinh.__init__(self, 2)
        print("Hinh chu nhat")
    def dt(self):
        a, b = self.canh
        return a*b

class tg(hinh):

    def __init__(self):
        hinh.__init__(self, 3)
        print("Hinh tam giac")
    def dt(self):
        a, b, c = self.canh
        if a+b>c and a+c>b and b+c>a:
            p = (a + b + c)/2
            return math.sqrt(p*(p-a)*(p-b)*(p-c))
        else:
            return -1

v = hv()
v.nhap()
v.incanh()
print(v.dt())

cn = hcn()
cn.nhap()
cn.incanh()
print(cn.dt())

t = tg()
t.nhap()
if t.dt() == -1:
    print("Khong la tam giac!")
else:
    t.incanh()
    print(t.dt())
