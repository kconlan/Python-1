'''
4. Implement a function to perform basic compression using the counts of repeated characters.
   For example, the string aabcccccaaa would become a2b1c5a3.
   If the compressed string would not become smaller than the original string,
   your method should return the original string.
'''


def compress(s):
    c = s[0]  # Compressed result
    ch = s[0] # Current character
    ct = 0    # Compression count
    
    for S in s:
        if S == ch:
            ct += 1
        else:
            c += str(ct) + S
            ch = S
            ct = 1

    c += str(ct)

    if len(c) > len(s):
        c = s

    return c

print(compress('aabcccccaaa'))
