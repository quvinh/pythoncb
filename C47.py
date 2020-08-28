f = open("file.txt","r")
print(f.read())
f.close()

lt = list()

f = open("file.txt","r")
while True:
    line = f.readline()
    line = line.replace("\n","")
    if not line:
        break
    else:
        x = line.split(" ")
        lt.append(x)
f.close()
#print(lt)

i = 0
for j in lt[i]:
    if int(lt[i][1])>100 and int(lt[i][2])<200:
        for k in lt[i]:
            print(k, end=", ")
    i += 1

        
