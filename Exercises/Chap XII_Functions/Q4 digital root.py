def root (n):
    dig = []
    while sum (dig) > 10:
        for i in range (len (str (n))):
            dig.append (int (str (n)[i]))
        print (sum (dig))
print (root (298383938))