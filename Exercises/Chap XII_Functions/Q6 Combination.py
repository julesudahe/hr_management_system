import math

def binom (n, k):
    return (math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

print (binom (4, 2))