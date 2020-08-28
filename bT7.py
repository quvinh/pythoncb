import array as arr
n=int(input("Nhap so phan tu"))
a=arr.array('i',[])
for i in range(0,n):
    a.append(int(input("Nhap ptu thu %d :"%(i+1))))
print("Mang da nhap:",a)
s=0
for i in range(n):
    s+=a[i]

print("Tong cac ptu:",s)
print("Max trong mang:",max(a))

print("Nhap vi tri can chen:")
k=int(input())
print("Nhap so can chen:")
p=int(input())

a.insert(k,p)
print(a)

print("Nhap vi tri can Xoa:")
d=int(input())
a.remove(d)
print(a)