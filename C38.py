ch = input("Nhap chuoi:")
ch = ch.strip()

while ch.find("  ") != -1:
    ch = ch.replace("  "," ")

print(ch.title())
