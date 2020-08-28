
def fibo(n):
    if n<2:
        return n
    return fibo(n-1)+fibo(n-2)
    
n=int(input("Nhap n:"))
li=[fibo(i) for i in range(1,n+1)]
print(li)
