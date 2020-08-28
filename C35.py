ch = input("Nhap chuoi:")

up = 0
low = 0
num = 0

for i in ch:
    if i.isdigit() == True:num +=1
    if i.isupper() == True:up +=1
    if i.islower() == True:low +=1

print("Do dai chuoi:",len(ch))
print("So chu so:%d\nSo chu hoa:%d\nSo chu thuong:%d"%(num,up,low))
