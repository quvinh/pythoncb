def gt(n):
    g=1
    for i in range (1,n+1):
        g*=i
    return g

a=int(input("Nhap so:"))
print(a,"! = ",gt(a))