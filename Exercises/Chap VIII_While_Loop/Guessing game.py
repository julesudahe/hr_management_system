from random import randint
loses = 0
gain = 0

while loses == 0 or gain == 200: 
    random_number = randint (1,6)
    guess = eval(input('Guess your number: '))
    if guess != random_number:
        loses = loses + 10
        print ('You lost $', 10, 'and you are remaining with, ', 100 - loses)
    elif guess == random_number:
        gain = gain + 9
        print ('You gained $', 9, 'and your current gain is, ', gain)
