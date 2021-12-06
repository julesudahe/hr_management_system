from string import punctuation

paragraph = open ('C:/Users/j.udahemuka/Desktop/Bboxx Splits/personal-projects/personal-python/Exercises/Chap XI/github_commands.txt').read()

paragraph = paragraph.lower()
for p in punctuation:
    paragraph = paragraph.replace(p,'')

separate_words = paragraph.split()

word_counter = {}
for w in separate_words:
    if w in word_counter:
        word_counter [w] = word_counter [w] + 1
    else:
        word_counter [w] = 1 

final_list = list(word_counter.items())
final_list.sort

for i in final_list:
    print (i)