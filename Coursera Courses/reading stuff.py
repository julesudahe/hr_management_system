from random import randint

with open ('C:/Users/j.udahemuka/Desktop/Bboxx Splits/personal-projects/personal-python/Coursera Courses/Example1.txt','r') as my_file:
    files = my_file.read()
print (files)

list_value = []
for i in range (1000):
    list_value.append(str(randint (1, 10000)))

print(list_value)
with open ('C:/Users/j.udahemuka/Desktop/Bboxx Splits/personal-projects/personal-python/Coursera Courses/Example2.txt','w') as my_second_file:
    for line in list_value:
        my_second_file.write(line)