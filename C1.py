a1 = float(input("Nhap a1:"))
b1 = float(input("Nhap b1:"))
c1 = float(input("Nhap c1:"))
a2 = float(input("Nhap a2:"))
b2 = float(input("Nhap b2:"))
c2 = float(input("Nhap c2:"))

D = a1*b2-a2*b1
Dx = c1*b2-c2*b1
Dy = a1*c2-a2*c1

if D==0:
    if Dx==0 and Dy==0:
        print("HPT vo so nghiem")
    else:
        print("HPT Vo nghiem")
else:
    print("HPT co nghiem:\nx = %.2f\ny = %.2f"%(Dx/D,Dy/D))
    

