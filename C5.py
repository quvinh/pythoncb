import math

x1 = float(input("Nhap x1:"))
y1 = float(input("Nhap y1:"))
x2 = float(input("Nhap x2:"))
y2 = float(input("Nhap y2:"))
x3 = float(input("Nhap x3:"))
y3 = float(input("Nhap y3:"))

a = math.sqrt((x1-x2)**2 + (y1-y2)**2)
b = math.sqrt((x1-x3)**2 + (y1-y3)**2)
c = math.sqrt((x2-x3)**2 + (y2-y3)**2)

if a+b>c and a+c>b and b+c>a:
    p = (a+b+c)/2
    print("Dien tich tam giac: %.2f\nChu vi tam giac:%.2f"
          %(math.sqrt(p*(p-a)*(p-b)*(p-c)),(a+b+c)))
else:
    print("Nhap sai du lieu!")
