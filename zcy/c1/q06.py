#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def hanoi_r(n, a, b, c):
    if n == 1:
        print('move 1 from {} to {}'.format(a, b))
        print('move 1 from {} to {}'.format(b, c))
        return 2

    k = hanoi_r(n-1, a, b, c)

    print('move {} from {} to {}'.format(n, a, b))

    k += hanoi_r(n-1, c, b, a)

    print('move {} from {} to {}'.format(n, b, c))

    k += hanoi_r(n-1, a, b, c)

    return k + 2

def show_hanoi_restricted(n):
    k = hanoi_r(n, 'left', 'mid', 'right')
    print('It will move {} steps.'.format(k))

def test(n):
    print('size:', n)
    show_hanoi_restricted(n)
    print('----')

def main():
    '''用栈来求解汉诺塔问题'''
    test(1)
    test(2)
    test(3)
    test(4)
    test(5)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
