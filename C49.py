f = open("file.txt", "r")
ch = f.read()
print(ch)
f.close()

lt = [i for i in ch.split(" ")]
s = list()
#print(sorted(lt, reverse=True))

for i in lt:
    s.append(int(i))

s2 = sorted(s, reverse = True)
print(s2)

f = open("ketqua.txt", "w")
f.write(str(s2))
f.close()
    
