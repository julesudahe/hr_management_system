from random import randint

def random_three_digit (n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    #rando_var = randint (range_start, range_end)
    str_rando_var = list(str(randint (range_start, range_end)))
    if '0' not in str_rando_var:
        return ''.join (str_rando_var)
    else:
        print ('Random value had 0')
        
print (random_three_digit(3))