# He phuong trinh
a1=float(input("Nhap a1:"))
b1=float(input("Nhap b1:"))
c1=float(input("Nhap c1:"))
a2=float(input("Nhap a2:"))
b2=float(input("Nhap b2:"))
c2=float(input("Nhap c2:"))

D=float(a1*b2-a2*b1)
Dx=float(c1*b2-c2*b1)
Dy=float(a1*c2-a2*c1)
if D==0:
    if Dx==0 and Dy==0:
        print("HPT Vo so nghiem")
    else:
        print("HPT Vo nghiem")
else:
    print("HPT co nghiem:\nx= ",Dx/D)
    print("y= ",Dy/D)
