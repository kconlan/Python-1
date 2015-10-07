import sys


def yesno(s=''):
    r = False
    try:
        yn = input(s + ' [Y/n] ')
    except EOFError:
        sys.exit()
    if yn != '' and yn[0].lower() == 'y':
        r = True
    return r

try:
    name = input('Hi, What is your name? ')
except EOFError:
    sys.exit()

print('Hello ' + name + '! Let\'s play a game!')

range_min = 0
range_max = 100
playing = True
target = (range_max - range_min) / 2

while playing:
    print('Think of random number from ' + str(range_min) +
          ' to ' + str(range_max) + ', and I\'ll try to guess it!')
    tries = 0
    while True:
        tries += 1
        if yesno('Is it ' + str(int(target)) + '?'):
            break
        else:
            if yesno('Is it less than ' + str(int(target)) + '?'):
                target -= 1
            else:
                target += 10
    print('Yeey! I got it in ' + str(tries) + ' tries!')
    if yesno('Do you want to play more?'):
        playing = True
print('Bye-bye')
