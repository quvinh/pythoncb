n=int(input('n= '))
s=0    
for i in range(1,n+1):
    s=s+1.0/(i*(i+1))
print('s= %.2f'%s)