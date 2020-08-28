import math
a = float(input("Nhap a:"))
b = float(input("Nhap b:"))
c = float(input("Nhap c:"))

if a==0:
    if b==0:
        if c==0:
            print("Pt VSN!")
        else:
            print("Pt VN!")
    else:
        print("Pt co nghiem: %.2f"%(-c/b))
else:
    d = b**2 - 4*a*c
    if d>0: print("Pt co 2 nghiem:\nx1 = %.2f\nx2 = %.2f"%((-b+math.sqrt(d))/(2*a),(-b-math.sqrt(d))/(2*a)))
    if d==0: print("Pt co nghiem: x = %.2f"%(-b/(2*a)))
    if d<0: print("Pt VN!")