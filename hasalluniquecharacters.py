'''
6. Implement a function to determine if a string has all unique characters.
   What if you cannot use additional structures?
'''


# HAHAHA! This one was too easy.
def hasAllUniqueCharacters(s):
    return ''.join(sorted(set(s))) == ''.join(sorted(s))

print(hasAllUniqueCharacters('Computer Programmer Numerical Control'))
print(hasAllUniqueCharacters('Film Or Tape Librarian'))
print(hasAllUniqueCharacters('Hotel Food Counter Worker'))
print(hasAllUniqueCharacters('ZYXWVUTSRQPONMLKJIHGFEDCBA'))
print(hasAllUniqueCharacters('zyxwvutsrqponmlkjihgfedcbaA'))
