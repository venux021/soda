#!/usr/bin/env python3
from collections import deque
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def serialize(t):
    if not t:
        return ''
    buf = []
    qu = deque()
    qu.append(t)
    buf.append(f'{t.value}!')
    while qu:
        f = qu.popleft()
        if f.lc:
            qu.append(f.lc)
            buf.append(f'{f.lc.value}!')
        else:
            buf.append('#!')
        if f.rc:
            qu.append(f.rc)
            buf.append(f'{f.rc.value}!')
        else:
            buf.append('#!')
    return ''.join(buf)

def deserialize(text):
    if not text:
        return
    seq = text.split('!')[:-1]
    qu = deque()
    root = Node(seq[0])
    qu.append(root)
    i = 1
    while qu:
        f = qu.popleft()
        lv = seq[i]
        i += 1
        if lv != '#':
            f.lc = Node(lv)
            qu.append(f.lc)
        rv = seq[i]
        i += 1
        if rv != '#':
            f.rc = Node(rv)
            qu.append(f.rc)
    return root

@testwrapper
def test(seq):
    tree = new_bitree_level(seq)
    print_tree(tree)
    text = serialize(tree)
    print(text)
    tree = deserialize(text)
    print_tree(tree)

def main():
    test([1,2,3,4,5,None,6])
    test([1,2,None,3])

if __name__ == '__main__':
    main()
