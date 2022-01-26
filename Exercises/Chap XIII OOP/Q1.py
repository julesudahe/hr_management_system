
class Investment:
    def __init__(self, p, i, n):
        self.p = p
        self.i = i 
        self.n = n
    def principal (self):
        return self.p*(1+self.i)**self.n 
    
e = Investment (40000000, 0.11, 15)

print (e.principal())
