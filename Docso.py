def doc(n):
    a=n//100
    b=(n//10)%10
    c=n%10
    
    if a==1:
        print("Mot tram",end=' ')
    if a==2:
        print("Hai tram",end=' ')
    if a==3:
        print("Ba tram",end=' ')
    if a==4:
        print("Bon tram",end=' ')
    if a==5:
        print("Nam tram",end=' ')
    if a==6:
        print("Sau tram",end=' ')
    if a==7:
        print("Bay tram",end=' ')
    if a==8:
        print("Tam tram",end=' ')
    if a==9:
        print("Chin tram",end=' ')


    if b==0 and c!=0:
        print("le",end=' ')
    if b==1:
        print("muoi",end=' ')
    if b==2:
        print("hai muoi",end=' ')
    if b==3:
        print("ba muoi",end=' ')
    if b==4:
        print("bon muoi",end=' ')
    if b==5:
        print("nam muoi",end=' ')
    if b==6:
        print("sau muoi",end=' ')
    if b==7:
        print("bay muoi",end=' ')
    if b==8:
        print("tam muoi",end=' ')
    if b==9: 
        print("chin muoi",end=' ')

    if c==0 and b==0:
        print(" ")    
    if c==1:
        print("mot")
    if c==2:
        print("hai")
    if c==3:
        print("ba")
    if c==4:
        print("bon")
    if c==5:
        print("nam")
    if c==6:
        print("sau")
    if c==7:
        print("bay")
    if c==8:
        print("tam")
    if c==9:
        print("chin")

n=int(input("Nhap 3 chu so:"))
print(doc(n))
