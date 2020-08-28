class Emp:
    species = "good"
    def __init__(self, ten, heso):
        self.hoten = ten
        self.hesoluong = heso
    def calSalary(self):
        return self.hesoluong*1300000

a = Emp("Vinh",5)
print(a.hoten)    
print(a.calSalary())
print(a.species)