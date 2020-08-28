x=int(input('x= '))
n=int(input('n= '))
s=0
for i in range(0,n+1):
    s=s+(-1)**(i+1)*(x/(2*i+1))
print('s= %.3f'%s)