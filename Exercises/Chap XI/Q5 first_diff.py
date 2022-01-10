def first_diff (string_1, string_2):

    
    if string_1 == string_2:
        print('The text is matching')
    elif len (string_1) == len (string_2) and string_2 != string_1:
        diff_1 = []
        for i in range (len(string_1)):
            if string_1 [i] != string_2 [i]:
                diff_1.append (string_1[i])
        print ('The text first different character is:', diff_1 [0])
    elif len (string_1) != len (string_2):
        diff = []
        max_value = [len(string_1), len(string_2)]
        new_string_1 = string_1 [:min(max_value)]
        new_string_2 = string_2 [:min(max_value)]
        if new_string_2 == new_string_1:
            print (max ([string_1, string_2])[len(new_string_1)])
        elif new_string_2 != new_string_1:
            for i in range (len (new_string_1)):
                if new_string_1 [i] != new_string_2 [i]:
                    diff.append (new_string_1 [i])
                    #return diff_2 [0]
            print ('The text first different character is:', diff [0])


print (first_diff(string_1=input('Enter your first value:'),string_2=input('Enter your second value:')))