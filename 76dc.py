class ch:
    def __init__(self):
        self.s = " "
    def getStr(self):
        self.s = input("Nhap chuoi: ")
    def printStr(self):
        print(self.s.upper())
n = ch()
n.getStr()
n.printStr()