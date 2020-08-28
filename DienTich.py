import math
x1=float(input("Nhap x1:"))
y1=float(input("Nhap y1:"))
x2=float(input("Nhap x2:"))
y2=float(input("Nhap y2:"))
x3=float(input("Nhap x3:"))
y3=float(input("Nhap y3:"))

a=math.sqrt((x2-x1)**2+(y2-y1)**2)
b=math.sqrt((x3-x1)**2+(y3-y1)**2)
c=math.sqrt((x3-x2)**2+(y3-y2)**2)

if a+b>c and a+c>b and b+c>a:
    p=(a+b+c)/2
    print("Chu vi:",p*2)
    print("Dien tich:",math.sqrt(p*(p-a)*(p-b)*(p-c)))
else:
    print("Khong tao thanh tam giac. Nhap lai!")
