from nltk.corpus import words
from itertools import product

# spellingbee letters
all_letters = ['i', 'v', 'c', 'l', 'b', 'n', 'e']

# special letter
special_letter = 'e'

# all words in english in lowercase
words = [x.lower() for x in words.words()]

# all words in line with the requirements (special character and length)
list = [x for x in words if (len(x) > 3) and (special_letter in x)]

# generate all possible permutations and print intersection with word list
for i in range(4, 8):
    print(set([''.join(x) for x in product(all_letters, repeat=i)])
          & set(list))
    i += i
