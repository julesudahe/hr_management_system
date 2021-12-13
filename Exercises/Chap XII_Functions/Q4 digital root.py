def digital_root (n):
    while dig < 10:
        dig = []
        for i in range (len (str (n))):
            dig.append (int (str(n)[i]))
        print (sum (dig))
print (digital_root (11111))