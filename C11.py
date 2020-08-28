
def HEX(n):
    lt = list()
    while n!=0:
        x=n//16
        y=n%16
        n=x
        if y<10 and y>=1 or y==0:
            lt.append(str(y))
        if y==10:
            lt.append("a")
        if y==11:
            lt.append("b")
        if y==12:
            lt.append("c")
        if y==13:
            lt.append("d")
        if y==14:
            lt.append("e")
        
        if y==15:
            lt.append("f")
    lt.reverse()
    print("".join(lt))
d = int(input("Nhap he 10:"))
print(hex(d))
HEX(d)

