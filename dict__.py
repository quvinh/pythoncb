thisdict = {
    "dictionary":"từ điển"
    ,"python":"con trăn"
    ,"information":"thông tin"
    ,"cat":"mèo"
}
for x,y in thisdict.items():
    print(x,y)

print("-----Tra từ------")
a = input("search: ")
if a in thisdict:
    x = thisdict.get(a)
    print(a,": ",x)
else:
    print("Khong co !")

print("-----Thêm từ------")
w = input("Word:")
m = input("Mean:")
thisdict[w] = m
print(thisdict)

print("-----Xóa từ------")
thisdict.pop(input("Delete word: "))
print(thisdict)

