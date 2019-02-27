#!/usr/bin/env python3
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def tree_display(t):
    if not t:
        print('Null tree')
        return
    do_display(t, 0, None)

def do_display(t, level, role):
    if not t:
        return
    do_display(t.rc, level + 1, 'right')
    print(' ' * 5 * level, end = ' ')
    if not role:
        print(f'H{t.value}H')
    elif role == 'left':
        print(f'^{t.value}^')
    else:
        print(f'V{t.value}V')
    do_display(t.lc, level + 1, 'left')

@testwrapper
def test(seq):
    tree = new_bitree_level(seq)
    print_tree(tree)
    tree_display(tree)

def main():
    test([1,2,3,4,None,5,6,None,7])

if __name__ == '__main__':
    main()
