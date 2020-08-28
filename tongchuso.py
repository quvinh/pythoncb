def tong(n):
    x=n
    s=0
    while x!=0:
        s=int(s+x%10)
        x/=10
    return s

x=int(input("Nhap chu so:"))
print("= ",tong(x))