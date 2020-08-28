import array as arr
n=int(input("Nhap so phan tu:"))
a=arr.array('i',[])
for i in range(0,n):
    a.append(int(input("Nhap ptu thu %d :"%(i+1))))
print("Mang da nhap:",a)
print("Nhap khoang x -> y:")
x=int(input())
y=int(input())
print("x->y:")
for i in range(n):
    if a[i]<=y and a[i]>=x :
        print(a[i])