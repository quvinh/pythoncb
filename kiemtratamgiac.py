#bai 10
import math
a=float(input('a= '))
b=float(input('b= '))
c=float(input('c= '))
if(a+b>c and a+c>b and b+c>a):
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('dien tich tam giac la: %.2f'%s)
else:
    print('khong la tam giac')