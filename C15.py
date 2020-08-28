import random
n = int(input("Nhap n:"))
lt = list()
for i in range(n):
    x = random.choice([i for i in range(1,100)])
    lt.append(x)

print(lt)
lt2 = set(lt)
print(lt2)
