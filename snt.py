x=int(input("Nhap 1 so nguyen:"))

if x<2:
    print(x," khong la so nguyen to")
else:

    mark=0
    for i in range(2,x):
        if x%i==0:
            mark=1

    if mark==1:
        print(x," khong la so nguyen to")
    else:
        print(x," la so nguyen to")

