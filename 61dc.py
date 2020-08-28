ch = input("Nhap chuoi:")
# n = dict()
# t=[ch.count(i) for i in ch]
# for i in range(len(ch)):
#     n[ch[i]]=t[i]
# print(n)

n = set(ch)
for i in n:
    print(i,":",ch.count(i))