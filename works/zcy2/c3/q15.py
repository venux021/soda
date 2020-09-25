#!/usr/bin/env python3
from collections import deque
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def is_bstree(t):
    last = [None]
    return _is_bstree(t, last)

def _is_bstree(t, last):
    if not t:
        return True
    if not _is_bstree(t.lc, last):
        return False
    if last[0] and last[0].value > t.value:
        return False
    last[0] = t
    return _is_bstree(t.rc, last)

def is_cbtree(t):
    if not t:
        return True
    qu = deque([t])
    only_left = False
    while qu:
        f = qu.popleft()
        if not f.lc and f.rc:
            return False
        if only_left and (f.lc or f.rc):
            return False
        if f.lc and not f.rc:
            only_left = True
        if f.lc:
            qu.append(f.lc)
        if f.rc:
            qu.append(f.rc)
    return True

@testwrapper
def test(seq):
    tree = new_bitree_level(seq)
    print_tree(tree)
    print('Is binary search tree:', is_bstree(tree))
    print('Is complete binary tree:', is_cbtree(tree))

def main():
    test([4,2,6,1,3,5,7])
    test([4,2,6,None,3,5,7])
    test([1,2,3,4,5,None,6])
    test([1,2,3,4,None,6])

if __name__ == '__main__':
    main()
