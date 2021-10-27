from math import log
add_value = eval(input('Enter n: '))
fraction = 0
for i in range (add_value):
    fraction = fraction + (1/(i+1))
    #print(fraction)
print('Your answer is: ',fraction+log(add_value))