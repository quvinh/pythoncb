#PT bac 2
import math

a=float(input("Nhap a:"))
b=float(input("Nhap b:"))
c=float(input("Nhap c:"))
if a==0:
    if b==0:
        if c==0: print("PT Vo so nghiem")
        else: print("PT Vo nghiem")
    else: print("PT co nghiem"+"\nx= ",-c/b)
else:
    d=b**2 - 4*a*c
    if d==0:
        print("====PT co nghiem:\nx= ",-b/(2*a))
    if d<0:
        print("====PT Vo nghiem")
    if d>0:
        print("====PT co 2 nghiem:\nx1= ",(-b+math.sqrt(d))/(2*a))
        print("x2= ",(-b-math.sqrt(d))/(2*a))
