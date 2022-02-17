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

word = input ('Enter your word per word to make your list: ')


final_list_word = Worldplay (word)
print (final_list_word.__init__())
print (final_list_word.end_with_s ())
print (final_list_word.start_with_s ())