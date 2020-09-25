#!/usr/bin/env python3
import math
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def count_complete_tree(t):
    if not t:
        return 0
    p = t
    n = 0
    while p.lc and p.rc:
        L = p.lc
        R = p.rc
        Ln = 0
        while L:
            Ln += 1
            L = L.rc
        Rn = 0
        while R:
            Rn += 1
            R = R.rc
        if Ln > Rn: # left is complete
            n += int(math.pow(2, Ln))
            p = p.rc
        else: # right is complete
            n += int(math.pow(2, Rn))
            p = p.lc
    if p.lc:
        n += 2
    else:
        n += 1
    return n

@testwrapper
def test(seq):
    tree = new_bitree_level(seq)
    print_tree(tree)
    n = count_complete_tree(tree)
    print(n)

def main():
    test([1,2,3,4,5,6,7])
    test([1,2,3,4,5])
    test([1,2,3,4,5,6])
    test([1,2,3,4])
    test([1,2,3,4,5,6,7,8,9,10])

if __name__ == '__main__':
    main()
