'''
2. A child is running a staircase with n steps, and can hop either 1 step, 2 steps, or 3 steps at a time.
   Implement a function to count how many possible ways the child can run up the stairs.
'''

# Of course there are ``better'' ways to do this.
def climb(n):
    p = 0
    q = 0
    while q < n:
        p += 1
        q += 1
    q = 0
    while q < n:
        p += 1
        q += 2
    q = 0
    while q < n:
        p += 1
        q += 3
    return p

for i in range(1, 10):
    print(str(i) + ': ' + str(climb(i)))
