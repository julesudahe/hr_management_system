def number_of_factors (m):
    count = 0
    list_factors = []
    for i in range (m):
        if m%(i+1) == 0:
            list_factors.append (i+1)
            count = count + 1
    print ('Your list is', list_factors, 'with', count, 'values')

print (number_of_factors(eval(input ('Enter your number:' ))))