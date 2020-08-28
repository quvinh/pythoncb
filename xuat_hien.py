import random

n=int(input("Nhap n: "))
# lt=random.sample(range(0,n),n)

lt1=[]
lt2=[]

for i in range(0,n):
    lt1.append(random.choice([i for i in range(1,10)]))
print("List vua nhap: ",lt1)

for i in range(0,n):
    if lt1.count(i) >1:
        lt2.append(i)

print("Cac phan tu xuat hien nhieu trong List: ",lt2)
