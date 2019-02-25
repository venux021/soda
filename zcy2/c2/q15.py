#!/usr/bin/env python3
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def tree2list(t):
    if not t:
        return (None, None)
    left_h, left_t = tree2list(t.lc)
    if left_t:
        left_t.rc = t
    t.lc = left_t

    right_h, right_t = tree2list(t.rc)
    if right_h:
        right_h.lc = t
    t.rc = right_h

    if not left_h:
        left_h = t
    if not right_t:
        right_t = t
    return (left_h, right_t)

def show_dlist(d, t):
    p = d
    while p:
        print(p.value, end = ' ')
        p = p.rc
    print('')
    p = t
    while p:
        print(p.value, end = ' ')
        p = p.lc
    print('')

@testwrapper
def test(pre_seq, in_seq):
    tree = new_bitree(pre_seq, in_seq)
    print_tree(tree)
    head, tail = tree2list(tree)
    show_dlist(head, tail)

def main():
    test([1], [1])
    test([1,2,4,5,3,6], [4,2,5,1,3,6])

if __name__ == '__main__':
    main()
