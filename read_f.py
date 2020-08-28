l = []
f = open("file.txt","r")
print(f.read())
f.close()

f = open("file.txt","r")
d = 0
while True:
    line = f.readline()
    line = line.replace("\n","")
    if not line:
        break
    else:
        d+=1
        a = line.split(" ")
        l.append(a)
# print(l)
s = 0
for i in range(len(l)):
    print(l[i])
    for j in range(i,len(l)):
        s += int(l[i][j])
f.close()


print("so dong: ",d)
print(s)
