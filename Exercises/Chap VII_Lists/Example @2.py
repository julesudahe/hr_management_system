from random import choice, randint, sample, shuffle
L=[]
for i in range (25):
    ##L.append(randint(1,100)) -- you can either use this one. 
    L=L+[randint(1,100)]
print (L)
print (len(L))
print (choice(L))
print (shuffle(L))
print (sample(L, 5))


