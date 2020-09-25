#!/usr/bin/env python3
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def max_sbitree(t):
    biggest = [0, None]
    do_find(t, biggest)
    return biggest[1]

def do_find(t, biggest):
    if not t:
        return 0
    left_size = do_find(t.lc, biggest)
    right_size = do_find(t.rc, biggest)
    left_ok = left_size == 0 or left_size > 0 and t.lc.value <= t.value
    right_ok = right_size == 0 or right_size > 0 and t.rc.value >= t.value
    if left_ok and right_ok:
        size = left_size + right_size + 1
        if size > biggest[0]:
            biggest[0] = size
            biggest[1] = t
        return size
    else:
        return -1

@testwrapper
def test(seq):
    tree = new_bitree_level(seq)
    print_tree(tree)
    xsb = max_sbitree(tree)
    print_tree(xsb)

def main():
    test([6,1,12,0,3,10,13,None,None,None,None,4,14,20,16,2,5,11,15])

if __name__ == '__main__':
    main()
