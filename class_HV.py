class hv:
    def __init__(self, x=0):
        self.x = x
    def dt(self):
        return self.x*self.x
    def cv(self):
        return self.x*4

c = float(input("Nhap canh Hinh vuong:"))
a = hv(c)
print(a.dt())
print(a.cv())