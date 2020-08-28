chuoi=input("Nhap chuoi:")

while( chuoi.find("  ") != -1):
    chuoi=chuoi.replace("  "," ")


# lt=chuoi.split(" ")

for i in chuoi:
    print(i)
print(len(chuoi))
# print(len(lt))

