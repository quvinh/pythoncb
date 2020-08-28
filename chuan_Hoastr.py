ch = input("Nhap chuoi:")
ch2 = ch.strip()
while (ch2.find("  ") != -1):
    ch2 = ch2.replace("  "," ")
ch2 = ch2.title()
print(ch2)