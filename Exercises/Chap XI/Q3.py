def sum_digit (num):
    num_list = []
    for i in range (len(str (num))):
        num_list.append(int(str (num)[i]))
    print (sum (num_list))
num = eval (input ('Enter your value:'))
print (sum_digit(num))