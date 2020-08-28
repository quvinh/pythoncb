ch = input("Nhap chuoi:")
x = input("Nhap chu cai x:")
ch2 = set(ch)
d = 0
for i in ch2:
    print(i, ": ", ch.count(i))
    
for i in ch:
    if i==x:
        d += 1
        

if d==0:
    print("%s ko xuat hien trong chuoi!"%x)
else:
    print("%s xuat hien :%d lan"%(x,d))
