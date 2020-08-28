import matplotlib as plt
import numpy as np

#plt.plot([1,2,3,4],[1,4,9,16])
#plt.show()
#plt.title("ALO ALO")
#plt.xlabel("X LABEL")
#plt.xlabel("X LABEL")

lt=[]
n=int(input("nhap so sinh vien: "))
for i in range (0,n):
    x=int(input("nhap diem  : "))
    lt.append(x)
gioi=0
kha=0
trungbinh=0
for i in lt:
    if i>=8:
        gioi=gioi+1
    elif i>=6:
        kha=kha+1
    elif i<=5:
        trungbinh=trungbinh+1
        

firms=["Gioi", "Kha","Trung Binh"]
a=[gioi,kha,trungbinh]
plt.bar(firms,a,color='red')
plt.title("bieu do diem")
plt.xlabel("sinh vien")
plt.ylabel("diem")
plt.show()
