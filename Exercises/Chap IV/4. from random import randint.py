from random import randint
count=0
for i in range (3):
    x=randint(1,10)
    y=randint(1,10)
    print('Question ',(i+1),': ',x,' x ',y,' = ',sep='', end=' ')
    question = eval (input ())
    if question==(x*y):
        print ('Correct')
        count = count + 1
    else:
        print ('Wrong, try again')
print ('Congratulations!! Your score is ', count, sep='')