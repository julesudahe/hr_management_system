from random import randint

def rectangle (n, m):
    for i in range (n):
        print ("*"*m)

n = randint (10,20)
m = randint (5, 20)
print ('The rectangle will have LENGTH:',n,'and WIDTH:', m)
print (rectangle(n,m))
