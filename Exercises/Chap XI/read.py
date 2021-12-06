from string import punctuation

text = open ('C:/Users/j.udahemuka/Desktop/Bboxx Splits/personal-projects/personal-python/Exercises/Chap XI/github_commands.txt').read()

text = text.lower()
for p in punctuation:
    text = text.replace(p,'')
words = text.split()

print ('words are: ', words)

d = {}
for w in words:
    if w in d:
        d[w] = d[w] + 1
    else:
        d[w] = 1

items = list(d.items())
items.sort
for i in items:
    print (i)