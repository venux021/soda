#!/usr/bin/env python3
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def is_balance(t):
    b, height = _is_balance(t)
    return b

def _is_balance(t):
    if not t:
        return (True, 0)
    bL, hL = _is_balance(t.lc)
    if not bL:
        return (False, 0)
    bR, hR = _is_balance(t.rc)
    if not bR:
        return (False, 0)
    height = max(hL, hR) + 1
    return (abs(hL - hR) <= 1, height)

@testwrapper
def test(seq):
    tree = new_bitree_level(seq)
    print_tree(tree)
    print('Is balance binary tree:', is_balance(tree))

def main():
    test([1,2,3,4,5,None,6])
    test([1,2,3,4,5,None,6,None,None,None,None,7])
    test([])

if __name__ == '__main__':
    main()
