from pickle import APPEND


class Worldplay:
    def __init__(self, string_word):
        self.string_word = string_word
    
    def word_with_lenght (self):
        word_lenght = []
        for i in range (len (self.string_word)):
            word_lenght = word_lenght.append (len (self.string_word))
        print (word_lenght)
    
    def start_with_s (self):
        start_with = []
        for i in range (len (self.string_word)):
            if self.string_word [i] == 's':
                start_with = start_with.append(len (self.string_word))
        print (start_with)
    
    def end_with_s (self):
        end_with = []
        for i in range (len (self.string_word)):
            if self.string_word [-len (self.string_word) + i] == 's':
                end_with = end_with.append (len (self.string_word))
        print (end_with)

list_word = []
while list_word != True:
    word = input ('Enter your word per word to make your list: ')
    if list_word != True:
        list_word = list_word.append (word)
    else:
        print ('Thanks')
print (list_word)

final_list_word = Worldplay (list_word)
print (final_list_word.end_with_s ())
print (final_list_word.start_with_s ())