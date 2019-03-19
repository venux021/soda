#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def nqueen(n):
    up_limit = (1 << n) - 1
    return do_process(up_limit, 0, 0, 0)

def do_process(up_limit, col_limit, left_limit, right_limit):
    if col_limit == up_limit:
        return 1
    pos = up_limit & (~(col_limit | left_limit | right_limit))
    res = 0
    while pos:
        right_most = pos & ((~pos) + 1)
        pos -= right_most
        res += do_process(up_limit, col_limit | right_most, 
                (left_limit | right_most) << 1,
                (right_limit | right_most) >> 1)
    return res

@testwrapper
def test(n):
    print(n, nqueen(n))

def main():
    for i in range(1,13):
        test(i)

if __name__ == '__main__':
    main()
