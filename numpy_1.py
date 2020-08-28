import numpy as np
n=2
m=3
x= np.array([(1,2,3), (3,4,5)])

for i in range(n):
    for j in range(m):
        x[i][j] = int(input("Nhap phantu:"))
print(x)
