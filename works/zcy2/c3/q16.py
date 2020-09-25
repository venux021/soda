#!/usr/bin/env python3
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def build_balance(seq):
    n = len(seq)
    if n == 0:
        return
    elif n == 1:
        return Node(value = seq[0])
    mid = n // 2
    left_seq = seq[0:mid]
    right_seq = seq[mid+1:]
    node = Node(value = seq[mid])
    node.lc = build_balance(left_seq)
    node.rc = build_balance(right_seq)
    return node

@testwrapper
def test(seq):
    print(seq)
    tree = build_balance(seq)
    print_tree(tree)

def main():
    test([1,2,3,4,5,6,7])
    test([1,2,3])
    test([1,2])
    test([1])

if __name__ == '__main__':
    main()
