import random as r
import string
import time

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxyz'
strg = string.lowercase

num_letters = input("How many letters do you want? ")
inpt = []
for i in range(num_letters):
    inpt.append(raw_input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, and 'l' for any letter: "))


#testing inputs
#print(letter_input_1+ letter_input_2+letter_input_3)
lst = []
def generator(letter_input):
    if letter_input == 'v':
        letter = r.choice(vowels)
    elif letter_input == 'c':
        letter = r.choice(consonants)
    elif letter_input == 'l':
        letter = r.choice(strg)
    else:
        letter = letter_input
    return letter

def gen_total(lsts):
    l_total = ""
    for lst in lsts:
        l_temp = generator(lst)
        l_total+=l_temp
    return l_total

#test = gen_total(letter_input_1, letter_input_2, letter_input_3)
for i in range(20):
    lst.append(gen_total(inpt))

for i in lst:
    print(i)
    time.sleep(1)
