def tong(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s

n=int(input("Nhap n:"))
print("Tong :",tong(n))