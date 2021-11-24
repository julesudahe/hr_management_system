from random import randint

secret_number = randint (1,50)
guess = 0

while guess != secret_number:
    print(eval(input('Enter your guess: ')))
else:
    print('You are correct!!!!!!!!!!!!!')