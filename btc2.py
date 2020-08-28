#50
import random
n = int(input("Nhap n:"))
lt = []
for i in range(n):
    x = random.choice([i for i in range(1,100)])
    lt.append(x)
print(lt)

m = 0
for i in lt:
    if i>m:
        m=i

print("Max = ",m)
