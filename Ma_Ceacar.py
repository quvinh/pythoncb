def compare1(s1, s2):
    for i in s1:
        if i == 0: s2.append("a")
        if i == 1: s2.append("b")
        if i == 2: s2.append("c")
        if i == 3: s2.append("d")
        if i == 4: s2.append("e")
        if i == 5: s2.append("f")
        if i == 6: s2.append("g")
        if i == 7: s2.append("h")
        if i == 8: s2.append("i")
        if i == 9: s2.append("j")
        if i == 10: s2.append("k")
        if i == 11: s2.append("l")
        if i == 12: s2.append("m")
        if i == 13: s2.append("n")
        if i == 14: s2.append("o")
        if i == 15: s2.append("p")
        if i == 16: s2.append("q")
        if i == 17: s2.append("r")
        if i == 18: s2.append("s")
        if i == 19: s2.append("t")
        if i == 20: s2.append("u")
        if i == 21: s2.append("v")
        if i == 22: s2.append("w")
        if i == 23: s2.append("x")
        if i == 24: s2.append("y")
        if i == 25: s2.append("z")

def encode(s1, k, s2):
    for i in s1:
        if i == "a":
            j = k%26
            s2.append(j)
        if i == "b":
            j = (1+k)%26
            s2.append(j)
        if i == "c":
            j = (2+k)%26
            s2.append(j)
        if i == "d":
            j = (3+k)%26
            s2.append(j)
        if i == "e":
            j = (4+k)%26
            s2.append(j)
        if i == "f":
            j = (5+k)%26
            s2.append(j)
        if i == "g":
            j = (6+k)%26
            s2.append(j)
        if i == "h":
            j = (7+k)%26
            s2.append(j)
        if i == "i":
            j = (8+k)%26
            s2.append(j)
        if i == "j":
            j = (9+k)%26
            s2.append(j)
        if i == "k":
            j = (10+k)%26
            s2.append(j)
        if i == "l":
            j = (11+k)%26
            s2.append(j)
        if i == "m":
            j = (12+k)%26
            s2.append(j)
        if i == "n":
            j = (13+k)%26
            s2.append(j)
        if i == "o":
            j = (14+k)%26
            s2.append(j)
        if i == "p":
            j = (15+k)%26
            s2.append(j)
        if i == "q":
            j = (16+k)%26
            s2.append(j)
        if i == "r":
            j = (17+k)%26
            s2.append(j)
        if i == "s":
            j = (18+k)%26
            s2.append(j)
        if i == "t":
            j = (19+k)%26
            s2.append(j)
        if i == "u":
            j = (20+k)%26
            s2.append(j)
        if i == "v":
            j = (21+k)%26
            s2.append(j)
        if i == "w":
            j = (22+k)%26
            s2.append(j)
        if i == "x":
            j = (23+k)%26
            s2.append(j)
        if i == "y":
            j = (24+k)%26
            s2.append(j)
        if i == "z":
            j = (25+k)%26
            s2.append(j)

def decode(s1, k, s2):
    for i in s1:
        if i == "a":
            j = (-k)%26
            s2.append(j)
        if i == "b":
            j = (1-k)%26
            s2.append(j)
        if i == "c":
            j = (2-k)%26
            s2.append(j)
        if i == "d":
            j = (3-k)%26
            s2.append(j)
        if i == "e":
            j = (4-k)%26
            s2.append(j)
        if i == "f":
            j = (5-k)%26
            s2.append(j)
        if i == "g":
            j = (6-k)%26
            s2.append(j)
        if i == "h":
            j = (7-k)%26
            s2.append(j)
        if i == "i":
            j = (8-k)%26
            s2.append(j)
        if i == "j":
            j = (9-k)%26
            s2.append(j)
        if i == "k":
            j = (10-k)%26
            s2.append(j)
        if i == "l":
            j = (11-k)%26
            s2.append(j)
        if i == "m":
            j = (12-k)%26
            s2.append(j)
        if i == "n":
            j = (13-k)%26
            s2.append(j)
        if i == "o":
            j = (14-k)%26
            s2.append(j)
        if i == "p":
            j = (15-k)%26
            s2.append(j)
        if i == "q":
            j = (16-k)%26
            s2.append(j)
        if i == "r":
            j = (17-k)%26
            s2.append(j)
        if i == "s":
            j = (18-k)%26
            s2.append(j)
        if i == "t":
            j = (19-k)%26
            s2.append(j)
        if i == "u":
            j = (20-k)%26
            s2.append(j)
        if i == "v":
            j = (21-k)%26
            s2.append(j)
        if i == "w":
            j = (22-k)%26
            s2.append(j)
        if i == "x":
            j = (23-k)%26
            s2.append(j)
        if i == "y":
            j = (24-k)%26
            s2.append(j)
        if i == "z":
            j = (25-k)%26
            s2.append(j)

print("___Ma Ceacar___")
str1 = input("Nhap chuoi:")
str2 = list()
str3 = list()
k = int(input("Nhap khoa k:"))
print("________________________________\n_1.Encode\n_2.Decode\n_0.Exit")
lc = int(input("Nhap lua chon: "))
while lc != 0:
    if lc == 1:
        for i in str1:
            print(i, end="")
        encode(str1, k, str2)
        compare1(str2, str3)
        print("\nEncode completed:")
        for i in str3:
            print(i, end="")
        break
    if lc == 2:
        for i in str1:
            print(i, end="")
        decode(str1, k, str2)
        compare1(str2, str3)
        print("\nDecode completed:")
        for i in str3:
            print(i, end="")
        break
    lc = int(input("Nhap lai lua chon (-_-): "))
