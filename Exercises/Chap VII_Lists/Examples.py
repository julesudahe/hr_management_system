from random import randint
L=[]
for i in range (50):
    L.append(randint(1,100))
    L=L+[randint(1,100)]
print(L)

print (sum(L))
print (L[-1])
print (L.reverse())