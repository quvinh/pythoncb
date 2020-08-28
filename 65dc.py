n = input("Nhap chuoi:")

# lt = n.replace(","," ")
lt = n.split(",")

for i in lt:
    if int(i)%2 != 0:
        print(i, end=" ")
       

