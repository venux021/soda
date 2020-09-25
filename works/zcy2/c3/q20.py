#!/usr/bin/env python3
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def max_dist(t):
    height, dist = _max_dist(t)
    return dist

def _max_dist(t):
    if not t:
        return (0, 0)
    left_h, left_d = _max_dist(t.lc)
    right_h, right_d = _max_dist(t.rc)
    self_dist = left_h + 1 + right_h
    return (max(left_h, right_h) + 1, max(left_d, right_d, self_dist))

@testwrapper
def test(seq):
    tree = new_bitree_level(seq)
    print_tree(tree)
    print(max_dist(tree))

def main():
    test([1,2,3,4,5,6,7])
    test([1,2,3,4,5,6,7,None,None,8])

if __name__ == '__main__':
    main()
