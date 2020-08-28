ch = input("Nhap chuoi:")
ch = ch.strip()
while ch.find("  ") != -1:
    ch = ch.replace("  "," ")
ch = ch.split(" ")
print(ch)
s = 0
for i in ch:
    if len(i) > 1:
        s += 1
print("So tu trong chuoi:",s)
