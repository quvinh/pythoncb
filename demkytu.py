
n=str(input("Nhap chuoi:"))


print(len(n))

alpha=0
digit=0
space=0
up=0
low=0
for i in n:
    if i.isalpha() == True:
        alpha+=1
    if i.isdigit() == True:
        digit+=1
    if i.isspace() == True:
        space+=1
    if i.isupper() == False:
        up+=1
    if i.islower() == True:
        low+=1


print("So luong chu: %d"%alpha)
print("So luong chu so: %d"%digit)
print("So luong khoang trang: %d"%space)
print("So luong chu viet hoa: %d"%up)
print("So luong chu viet thuong: %d"%low)
