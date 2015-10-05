'''
1. Given an NxN matrix, write a function that would rotate it
by 90 degrees clock-wise or counter clockwise.
'''


# Rotate n clockwise or counter-clockwise
# If d == 0, clockwise
# If d == 1, counter-clockwise
# Else no change
def rotate(n, d):
    m = n
    if d == 0:
        m = zip(*m[::-1])
    elif d == 1:
        m = list(zip(*m))[::-1]
    return m


def matrixPrint(m):
    for n in m:
        for o in n:
            print(str(o) + ' ', end='')
        print('\n')

m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
matrixPrint(m)
print('Clockwise:')
matrixPrint(rotate(m, 0))
print('Counter-Clockwise:')
matrixPrint(rotate(m, 1))
