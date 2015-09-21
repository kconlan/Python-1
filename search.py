#!/usr/bin/python2

# Thanks to: http://www.artima.com/weblogs/viewpost.jsp?thread=4829
#
from __future__ import print_function
import sys
import getopt


class Usage(object):

    def __init__(self, message):
        self.message = message


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h', ['help'])
    except getopt.GetoptError as err:
        # print help information and exit:
        raise Usage(err)
        sys.exit(2)

    for o, a in opts:
        if o in ('-h', '--help'):
            print('Usage: search.py <filename>')
            sys.exit()
        else:
            assert False, 'Unrecognized option'

    if len(args) < 1:
        print('Usage: search.py <filename>')
        sys.exit()

    with open(args[0], 'r') as f:
        contents = sorted(f.read().splitlines())

    user_argv = raw_input('prompt:')

    line_nr = len(contents) - 1
    tries = -1
    while tries < line_nr:
        tries += 1
        if contents[tries].find(user_argv) != -1:
            print('Match found on: ' + str(tries) + ':')
            print(contents[tries])
            return

    print('No matches found.')

if __name__ == '__main__':
    sys.exit(main())
