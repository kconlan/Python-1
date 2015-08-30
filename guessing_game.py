#!/usr/bin/python2
range_min = 1
range_max = 100
target = (range_max - range_min) / 2
name = raw_input('Hi, What is your name? ')
playing = True
print 'Hello ' + name + '! Let\'s play a game!'
while playing:
    print 'Think of random number from ' + str(range_min) + \
            ' to ' + str(range_max) + ', and I\'ll try to guess it!'
    tries = 0
    while True:
        tries += 1
        s = 'Is it ' + str(target) + ' (yes/no)? '
        yn = raw_input(s)
        if yn[0] == 'y' or yn[0] == 'Y':
            break
        else:
            s = 'Is it less than ' + str(target) + ' (yes/no)? '
            yn = raw_input(s)
            if yn[0] == 'y' or yn[0] == 'Y':
                target -= 1
            else:
                target += 10
    print 'Yeey! I got it in ' + str(tries) + ' tries!'
    yn = raw_input('Do you want to play more? ')
    if yn[0] == 'y' or yn[0] == 'Y':
        playing = True
print 'Bye-bye'
