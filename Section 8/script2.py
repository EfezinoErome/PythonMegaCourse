import random as r
import string

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxyz'
strg = string.lowercase

letter_input_1 = raw_input("What letter do you want? Enter 'v' " +
"for vowels, 'c' for consonants, and 'l' for any letter: ")
letter_input_2 = raw_input("What letter do you want? Enter 'v' " +
"for vowels, 'c' for consonants, and 'l' for any letter: ")
letter_input_3 = raw_input("What letter do you want? Enter 'v' " +
"for vowels, 'c' for consonants, and 'l' for any letter: ")

#testing inputs
#print(letter_input_1+ letter_input_2+letter_input_3)

def generator(letter_input):
    if letter_input == 'v':
        letter = r.choice(vowels)
    elif letter_input == 'c':
        letter = r.choice(consonants)
    elif letter_input == 'l':
        letter = r.choice(strg)
    else:
        letter = letter_input_1
    return letter

letter1 = generator(letter_input_1)
letter2 = generator(letter_input_2)
letter3 = generator(letter_input_3)

let = letter1+letter2+letter3
print(let)


