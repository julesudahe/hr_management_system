def sum_digit (num):
    if(num < 10):
        return num

    num = num % 10 + sum_digit(num//10)
    return sum_digit(num)

num = eval (input ('Enter your value:'))
print (sum_digit(num))