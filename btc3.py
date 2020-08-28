#62
ch = input("Nhap chuoi:")
ch2 = set(ch)

for j in ch2:
    print(j," :",ch.count(j))

print("so chu cai 'x'")
for i in ch2:
    if i == str("x"):
        print(i," :",ch.count(i))
