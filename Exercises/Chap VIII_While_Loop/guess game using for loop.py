from ctypes import pythonapi
from random import randint
secret_number = randint(1,100)

for i in range (5):
    guess = eval(input('Enter your guess: '))
    if guess > secret_number:
        print ('HIGH', 4-i, 'guess left')
    elif guess < secret_number:
        print ('LOWER', 4-i, 'guess left')
    else:
        print ('You got it!!!!!')
        break
else:
    print ('You lost. The correct answer is: ', secret_number)