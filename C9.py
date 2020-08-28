def he2(n):
    lt = list()
    while n!=0:
        b = n%2
        x = n//2
        n = x
        lt.append(str(b))
    lt.reverse()
    print("".join(lt))
    

d = int(input("Nhap DEC:"))
he2(d)
