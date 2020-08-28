
lt = list()
f = open("doc.txt","r")

while True:
    line = f.readline()
    line = line.replace("\n","")
    if not line:
        break
    else:
        a = line.split(" ")
        lt.append(a)
f.close()
for i in range(len(lt)):
    for j in lt[i]:
        print(j,end=" ")
    print()

for i in range(len(lt)):
    for j in range(len(lt[i])):
        for k in range(len(lt[i])):
            if lt[i][j] < lt[k][j]:
                       tg = lt[i][j]
                       lt[i][j] = lt[k][j]
                       lt[k][j] = tg

for i in range(len(lt)):
    for j in lt[i]:
        print(j,end=" ")
    print()


