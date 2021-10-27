setense = input('Enter your text: ')
count = 0
for i in range (len(setense)):
    if setense[i] == ' ':
        count=count+1
print ('Number of words are: ',count+1)