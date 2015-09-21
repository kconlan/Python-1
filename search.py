#!/usr/bin/python2

from __future__ import print_function
import sys
import getopt


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h', ['help'])
    except:
        print('Usage: search.py [-h] <filename>')
        return 1

    for o, a in opts:
        if o in ('-h', '--help'):
            print('Usage: search.py <filename>')
            return 1
        else:
            assert False, 'Unrecognized option'
            return 1

    if len(args) < 1:
        print('Usage: search.py <filename>')
        return 1

    with open(args[0], 'r') as f:
        lines = sorted(f.read().splitlines())

    user_input = raw_input('prompt:')
    user_argv = user_input.split(' ')
    _and = False
    _or = False

    if len(user_argv) == 3:
        if user_argv[1].lower() == 'and':
            _and = True
        elif user_argv[1].lower() == 'or':
            _or = True

    if _and or _or:
        if user_argv[0] == user_argv[2]:
            print('Error: search terms must be unique.')

    line_nr = len(lines) - 1
    tries = -1
    matches = 0
    while tries < line_nr:
        tries += 1
        if lines[tries].find(user_input) != -1:
            matches += 1
            print('Match found: ' + lines[tries])
        if _and and (lines[tries].find(user_argv[0]) != -1 and
                     lines[tries].find(user_argv[2]) != -1):
            matches += 1
            print('Match found (and): ' + lines[tries])
        if _or and (lines[tries].find(user_argv[0]) != -1 or
                    lines[tries].find(user_argv[2]) != -1):
            matches += 1
            print('Match found (or): ' + lines[tries])

    if matches == 0:
        print('No matches found.')
    else:
        print('Found ' + str(matches) + ' matches.')

    return matches < 1

if __name__ == '__main__':
    sys.exit(main())
