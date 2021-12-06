from random import randint
your_money = 0

while 0 <= your_money <= 200:
    random_number = randint (1,6)
    guess = eval(input('Guess your number: '))
    if guess != random_number:
        your_money = your_money + 10
        print ('You lost $', 10, 'and you are remaining with, ', 100 - your_money)
    elif guess == random_number:
        your_money = your_money + 9
        print ('You gained $', 9, 'and your current gain is, ', your_money)
