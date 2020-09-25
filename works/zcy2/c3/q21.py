#!/usr/bin/env python3
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def pre_in(spre, sin):
    if not spre:
        return
    root_v = spre[0]
    node = Node(root_v)
    i = sin.index(root_v)
    left_size = i
    right_size = len(sin) - i - 1
    if left_size > 0:
        node.lc = pre_in(spre[1:1+left_size], sin[:i])
    if right_size > 0:
        node.rc = pre_in(spre[1+left_size:], sin[i+1:])
    return node

def in_post(sin, spost):
    if not sin:
        return
    root_v = spost[-1]
    node = Node(root_v)
    i = sin.index(root_v)
    left_size = i
    right_size = len(sin) - i - 1
    if left_size > 0:
        node.lc = in_post(sin[:i], spost[:left_size])
    if right_size > 0:
        node.rc = in_post(sin[i+1:], spost[left_size:-1])
    return node

def pre_post(spre, spost):
    if not spre:
        return
    root_v = spre[0]
    node = Node(root_v)
    if len(spre) == 1:
        return node
    lcv = spre[1]
    rcv = spost[-2]
    ir = spre.index(rcv)
    left_size = ir - 1
    right_size = len(spre) - ir
    if left_size > 0:
        node.lc = pre_post(spre[1:ir], spost[:left_size])
    if right_size > 0:
        node.rc = pre_post(spre[ir:], spost[left_size:-1])
    return node

@testwrapper
def test(spre, sin, spost):
    print(spre, sin, spost)
    t1 = pre_in(spre, sin)
    print_tree(t1)
    t2 = in_post(sin, spost)
    print_tree(t2)
    t3 = pre_post(spre, spost)
    print_tree(t3)

def main():
    test([1,2,4,5,3,6,7], [4,2,5,1,6,3,7], [4,5,2,6,7,3,1])

if __name__ == '__main__':
    main()
