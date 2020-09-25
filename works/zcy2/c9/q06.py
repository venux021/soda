#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

down = 1
up = 2

def fold_line(n):
    do_fold_line(1, n, down)

def do_fold_line(m, n, flag):
    if m > n:
        return
    do_fold_line(m+1, n, down)
    print('down' if flag == down else 'up')
    do_fold_line(m+1, n, up)

@testwrapper
def test(n):
    print(n)
    fold_line(n)

def main():
    test(1)
    test(2)
    test(5)

if __name__ == '__main__':
    main()
