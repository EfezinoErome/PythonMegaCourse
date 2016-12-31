import random as r
import string

def generator():
    strg = string.lowercase
    letter1 = r.choice(strg)
    letter2 = r.choice(strg)
    letter3 = r.choice(strg)
    name = letter1+letter2+letter3
    return name

print(generator())



