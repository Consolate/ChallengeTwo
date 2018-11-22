# this is a function defination
#takes the string as input and return a string with vowels
def vowel(sentence):
    vowels = ["a","e","i","o","u"]
    word = sentence
    list(word)
    new_list= tuple(word)
    new_string=''
    for x in new_list:
        if x in vowels:
            new_string +=x
    print (new_string) 
    count=0
    for x in new_string:
        if x in vowels:
            new_string += x
            new_tuple= tuple()
            print(count)
vowel('this is consolate') 

if x in vowels:
            if x in new_string:
                count += 1
                if x not in new_string: