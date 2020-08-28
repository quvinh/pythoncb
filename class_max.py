class Max:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
    def lonnhat(self):
        return max(self.a,max(self.b, self.c))

m = Max(2, 9)
n = Max(5, 7, 1)
print(m.lonnhat(), " ", n.lonnhat())