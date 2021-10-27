setense = input('Enter your formula: ')
count = 0
count1 = 0
for i in range (len(setense)):
    if setense[i] == '(':
        count=count+1
    elif setense[i] == ')':
        count1=count1+1
if count1!=count:
    print ('Parenthese is missing')
else:
    print(setense)