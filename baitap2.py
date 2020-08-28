def uc(x, y):
    a = abs(x)
    b = abs(y)
    while a!=b:
        if a>b:
            a = a-b
        else:
            b = b-a
    return a
class ps:
    def __init__(self, t=0, m=1):
        self.t = t
        self.m = m
    def rg(self):
        return ps(self.t//uc(self.t, self.m), self.m//uc(self.t, self.m))
    def nhap(self):
        self.t = int(input("Nhap tu so:"))
        self.m = int(input("Nhap mau so:"))
    def __str__(self):
        return "{0} / {1}".format(self.t, self.m)
    def __add__(self, other):
        t = self.t*other.m + other.t*self.m
        m = self.m * other.m
        return ps(t, m)
    def __sub__(self, other):
        t = (self.t*other.m) - (other.t*self.m)
        m = self.m * other.m
        return ps(t, m)
    def __mul__(self, other):
        t = self.t * other.t
        m = self.m * other.m
        return ps(t, m)
    def __truediv__(self, other):
        t = self.t * other.m
        m = self.m * other.t
        return ps(t, m)

 
    
p = ps()
p.nhap()
p2 = ps()
p3 = ps()
p2.nhap()
p3 = p + p2
p4 = p - p2
p5 = p * p2
p6 = p / p2
print(p3.rg())
print(p4.rg())
print(p5.rg())
print(p6.rg())
