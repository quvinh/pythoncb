class animal:
    def __init__(self):
        print("Animal created")
    def whoAmI(self):
        print("animal")
    def eat(self):
        print("eating")

class dog(animal):
    def __init__(self):
        animal.__init__(self)
        print("Dog created")
    def whoAmI(self):
        print("dog")
    def bark(self):
        print("sua!")

class cat(animal):
    def __init__(self):
        animal.__init__(self)
        print("Cat created")
    def whoAmI(self):
        print("Cat")
    def meo(self):
        print("moew !")


d = dog()
d.whoAmI()
d.eat()
d.bark()
print("------")
c = cat()
c.whoAmI()
c.eat()
c.meo()