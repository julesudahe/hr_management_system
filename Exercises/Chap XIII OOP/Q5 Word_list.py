from string import punctuation

class Worldplay:
    def __init__(self, words):
        for c in punctuation:
            words = words.replace (c, '')
        words = words.lower ()
        self.string_word = words.split ()
   
    def word_with_lenght (self):
        word_lenght = []
        for i in range (len (self.string_word)):
            word_lenght.append (len (self.string_word [i]))
        print ('Lenght of words in our list is: ', word_lenght)
    
    def start_with_s (self):
        start_with = []
        for i in range (len (self.string_word)):
            if self.string_word [i] [0] == 's':
                start_with.append(self.string_word [i])
        print ('Words that starts with S: ', start_with)
    
    def end_with_s (self):
        end_with = []
        for i in range (len (self.string_word)):
            if self.string_word [i] [-1] == 's':
                end_with.append (self.string_word [i])
        print ('Word that ends with S: ', end_with)

words = input ('Enter your word per word to make your list: ')


final_list_word = Worldplay (words)
print (final_list_word.string_word)
print (final_list_word.word_with_lenght())
print (final_list_word.start_with_s ())
print (final_list_word.end_with_s ())
