import random
import math
n = int(input("Nhap n:"))
x = random.sample([i for i in range(1,100)],n)
y = random.sample([i for i in range(1,100)],n)
print(x)
print(y)

tx = 0
ty = 0
for i in range(n):
    tx += x[i]**2
    ty += y[i]**2

print("Vecto X = %.2f"%math.sqrt(tx))
print("Vecto Y = %.2f"%math.sqrt(ty))

z = list()
for i in range(n):
    a = x[i] + y[i]
    z.append(a)

print("Z = ",z)
