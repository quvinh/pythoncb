#def fi(n):
def fi(n):
    if n==1 or n==2:
        return 1
    
    f0=1
    f1=1
    for i in range(3,n+1):
        fn=f0+f1
        f0=f1
        f1=fn
    return fn
n=int(input("Nhap n:"))
li=[fi(i) for i in range(1,n+1)]

print(li)
#li=[fi(i) for i in range(1,n+1)]

