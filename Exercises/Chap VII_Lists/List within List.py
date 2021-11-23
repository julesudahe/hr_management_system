from string import punctuation

paragraph = input('Enter your paragraph: ')

for c in punctuation:
    paragraph = paragraph.replace(c,'')
paragraph = paragraph.lower()
new_paragraph = paragraph.split()

print ('A appeared ',new_paragraph.count('a'),'times')
print ('AN appeared ',new_paragraph.count('an'),'times')
print ('THE appeared ',new_paragraph.count('the'),'times')
