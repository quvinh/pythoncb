import random
import math

n=int(input("Nhap n: "))
lt=[]
s=0

for i in range(0, n):
    lt.append(random.choice([i for i in range(0,10)]))

print(lt)

for i in range(0, n):
    s+=(lt[i]**2)

print(s)
print("T = %.2f"%math.sqrt(s))
