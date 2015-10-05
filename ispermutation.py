'''
5. Given two strings, write a function to decide is one is
   the permutation of the other.
'''


def isPermutation(s1, s2):
    weightS1 = 0
    weightS2 = 0
    for s in s1:
        weightS1 += ord(s)
    for s in s2:
        weightS2 += ord(s)
    return weightS1 == weightS2

print(isPermutation('racecar', 'rraacce'))
