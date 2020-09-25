#!/usr/bin/env python3
from collections import deque
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def print_level(t):
    if not t:
        return
    qu = deque([(t,1)])
    last_level = 0
    while qu:
        node, level = qu.popleft()
        if level > last_level:
            print('')
        last_level = level
        print(node.value, end = ' ')
        if node.lc:
            qu.append((node.lc, level + 1))
        if node.rc:
            qu.append((node.rc, level + 1))
    print('')

def print_zigzag(t):
    if not t:
        return
    cur_dir = 1 # left to right, if 2 then right to left
    qu = deque([(t,1)])
    last_level = 0
    while qu:
        if cur_dir == 1:
            node, level = qu.popleft()
            if level % 2 == 0:
                cur_dir = 2
                qu.appendleft((node, level))
                continue
        else:
            node, level = qu.pop()
            if level % 2 == 1:
                cur_dir = 1
                qu.append((node, level))
                continue
        if level > last_level:
            print('')
        last_level = level
        print(node.value, end = ' ')
        if cur_dir == 1:
            if node.lc:
                qu.append((node.lc, level + 1))
            if node.rc:
                qu.append((node.rc, level + 1))
        else:
            if node.rc:
                qu.appendleft((node.rc, level + 1))
            if node.lc:
                qu.appendleft((node.lc, level + 1))
    print('')

@testwrapper
def test(seq):
    tree = new_bitree_level(seq)
    print_tree(tree)
    print_level(tree)
    print_zigzag(tree)

def main():
    test([1,2,3,4,None,5,6,None,None,7,8])

if __name__ == '__main__':
    main()
