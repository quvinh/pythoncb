def ucln(a,b):
    x = abs(a)
    y = abs(b)
    while x!=y:
        if x>y:x-=y
        else: y-=x
    return x

def compare1(str,ch3):
    for ex in str:
        if ex==0:ch3.append("a")
        if ex==1:ch3.append("b")
        if ex==2:ch3.append("c")
        if ex==3:ch3.append("d")
        if ex==4:ch3.append("e")
        if ex==5:ch3.append("f")
        if ex==6:ch3.append("g")
        if ex==7:ch3.append("h")
        if ex==8:ch3.append("i")
        if ex==9:ch3.append("j")
        if ex==10:ch3.append("k")
        if ex==11:ch3.append("l")
        if ex==12:ch3.append("m")
        if ex==13:ch3.append("n")
        if ex==14:ch3.append("o")
        if ex==15:ch3.append("p")
        if ex==16:ch3.append("q")
        if ex==17:ch3.append("r")
        if ex==18:ch3.append("s")
        if ex==19:ch3.append("t")
        if ex==20:ch3.append("u")
        if ex==21:ch3.append("v")
        if ex==22:ch3.append("w")
        if ex==23:ch3.append("x")
        if ex==24:ch3.append("y")
        if ex==25:ch3.append("z")

def encode(str,x,y,ch2):
    # ch2 = list()
    for i in str:
        if i == "a":
            j = y%26
            ch2.append(j)
        if i == "b":
            j = (x+y)%26
            ch2.append(j)
        if i == "c":
            j = (2*x+y)%26
            ch2.append(j)
        if i == "d":
            j = (3*x+y)%26
            ch2.append(j)
        if i == "e":
            j = (4*x+y)%26
            ch2.append(j)
        if i == "f":
            j = (5*x+y)%26
            ch2.append(j)
        if i == "g":
            j = (6*x+y)%26
            ch2.append(j)
        if i == "h":
            j = (7*x+y)%26
            ch2.append(j)
        if i == "i":
            j = (8*x+y)%26
            ch2.append(j)
        if i == "j":
            j = (9*x+y)%26
            ch2.append(j)
        if i == "k":
            j = (10*x+y)%26
            ch2.append(j)
        if i == "l":
            j = (11*x+y)%26
            ch2.append(j)
        if i == "m":
            j = (12*x+y)%26
            ch2.append(j)
        if i == "n":
            j = (13*x+y)%26
            ch2.append(j)
        if i == "o":
            j = (14*x+y)%26
            ch2.append(j)
        if i == "p":
            j = (15*x+y)%26
            ch2.append(j)
        if i == "q":
            j = (16*x+y)%26
            ch2.append(j)
        if i == "r":
            j = (17*x+y)%26
            ch2.append(j)
        if i == "s":
            j = (18*x+y)%26
            ch2.append(j)
        if i == "t":
            j = (19*x+y)%26
            ch2.append(j)
        if i == "u":
            j = (20*x+y)%26
            ch2.append(j)
        if i == "v":
            j = (21*x+y)%26
            ch2.append(j)
        if i == "w":
            j = (22*x+y)%26
            ch2.append(j)
        if i == "x":
            j = (23*x+y)%26
            ch2.append(j)
        if i == "y":
            j = (24*x+y)%26
            ch2.append(j)
        if i == "z":
            j = (25*x+y)%26
            ch2.append(j)

def search(x):
    for i in range(1,27):
        if i*x%26 == 1:
            return i

def decode(str, x, y, ch2):
    xx = search(x)
    for i in str:
        if i == "a":
            j = xx*(-y)%26
            ch2.append(j)
        if i == "b":
            j = xx*(1-y)%26
            ch2.append(j)
        if i == "c":
            j = xx*(2-y)%26
            ch2.append(j)
        if i == "d":
            j = xx*(3-y)%26
            ch2.append(j)
        if i == "e":
            j = xx*(4-y)%26
            ch2.append(j)
        if i == "f":
            j = xx*(5-y)%26
            ch2.append(j)
        if i == "g":
            j = xx*(6-y)%26
            ch2.append(j)
        if i == "h":
            j = xx*(7-y)%26
            ch2.append(j)
        if i == "i":
            j = xx*(8-y)%26
            ch2.append(j)
        if i == "j":
            j = xx*(9-y)%26
            ch2.append(j)
        if i == "k":
            j = xx*(10-y)%26
            ch2.append(j)
        if i == "l":
            j = xx*(11-y)%26
            ch2.append(j)
        if i == "m":
            j = xx*(12-y)%26
            ch2.append(j)
        if i == "n":
            j = xx*(13-y)%26
            ch2.append(j)
        if i == "o":
            j = xx*(14-y)%26
            ch2.append(j)
        if i == "p":
            j = xx*(15-y)%26
            ch2.append(j)
        if i == "q":
            j = xx*(16-y)%26
            ch2.append(j)
        if i == "r":
            j = xx*(17-y)%26
            ch2.append(j)
        if i == "s":
            j = xx*(18-y)%26
            ch2.append(j)
        if i == "t":
            j = xx*(19-y)%26
            ch2.append(j)
        if i == "u":
            j = xx*(20-y)%26
            ch2.append(j)
        if i == "v":
            j = xx*(21-y)%26
            ch2.append(j)
        if i == "w":
            j = xx*(22-y)%26
            ch2.append(j)
        if i == "x":
            j = xx*(23-y)%26
            ch2.append(j)
        if i == "y":
            j = xx*(24-y)%26
            ch2.append(j)
        if i == "z":
            j = xx*(25-y)%26
            ch2.append(j)

print("___Ma affine___")
str1 = input("Nhap chuoi:")
str2 = list()
str3 = list()
print("Nhap khoa K(a,b)")
a = int(input("Nhap a:"))
b = int(input("Nhap b:"))
while ucln(a, b) != 1:
    a = int(input("Nhap a:"))
    b = int(input("Nhap b:"))
print("________________________________\n_1.Encode\n_2.Decode\n_0.Exit")
lc = int(input("Nhap lua chon: "))
while lc != 0:
    if lc == 1:
        for i in str1:
            print(i, end="")
        encode(str1, a, b, str2)
        compare1(str2, str3)
        print("\nEncode completed:")
        for i in str3:
            print(i, end="")
        break
    if lc == 2:
        for i in str1:
            print(i, end="")
        decode(str1, a, b, str2)
        compare1(str2, str3)
        print("\nDecode completed:")
        for i in str3:
            print(i, end="")
        break
    lc = int(input("Nhap lai lua chon (-_-): "))


