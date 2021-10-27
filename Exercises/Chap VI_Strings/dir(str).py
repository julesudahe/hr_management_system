setense = input('Enter your string : ')
print ('Number of characters are : ', len(setense))
for i in range (10):
    print((i+1),'. ', setense, sep='')
print(setense[0])
print(setense[0:3])
print(setense[-3:])
for i in range (len(setense)):
    print(setense[-(i+1)],end='')
print('')

if len(setense)>=6:
    print(setense[6])
else:
    print('Your word doesn\'t have sever characters')
print(setense.upper())
print(setense.replace('a','e'))
