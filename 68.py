ch = (input("Nhập chuỗi:"))
lt = [i for i in ch.split(" ")]
print(lt)
print(", ".join(sorted(list(lt))))

ch2 = set(lt)
for i in ch2:
    print(i,": ",lt.count(i))
