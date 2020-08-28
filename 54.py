import random
n = int(input("Nhập N số:"))

while n<0:
    n = int(input("Nhập N số:"))

lt = []
for i in range(n):
    lt.append(random.choice([i for i in range(100)]))

print("Tổng các phần tử: %d"%len(lt))
print(lt)

lt2 = []
for i in lt:
    if lt.count(i)>=2:
        lt2.append(i)

a = set(lt2)
print("_Các pt xuất hiện hơn 2 lần:")
print(a)

