from random import randint
secret_number = randint(1,100)
num_guess = 0
num = 0
while secret_number != num_guess and num <= 4:
    num_guess = eval(input('Enter your guess (1-100): '))
    num = num + 1
    if num_guess > secret_number:
        print('HIGH. ', 5-num, 'guess left.')
    elif num_guess < secret_number:
        print('LOWER. ', 5-num, 'guess left.')
    else:
        print ('You got it!!!!!')
if num == 5 and num_guess != secret_number:
    print ('You lose. The correct number is: ', secret_number)