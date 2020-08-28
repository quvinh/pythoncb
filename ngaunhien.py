import random
li = random.sample([i for i in range(100,1001) if i%7==0],10)
print(li)
print(len(li))
print(sum(li))