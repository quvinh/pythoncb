import random
lt=random.sample([i for i in range(1,100)],10)
print(lt)
t=0
for i in lt:
    for j in range(2,i):
        if i%j : break
    else: t+=i 

print("tong cac so nguyen to :",t)

    