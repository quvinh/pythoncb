n=float(input("Nhap so km:"))
s=0
t1=15000
if n<=1:
    s=t1
if n>2:
    t2=t1 + (n-1)*13500
    s=t2
if n>5:
    t3=t2 + (n-5)*11000
    s=t3
if n>120:
    t=t3 + (n-120)*t3*0.1
    s=t
print(s)
