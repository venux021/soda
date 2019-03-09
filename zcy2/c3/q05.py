#!/usr/bin/env python3
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def morris_in(t):
    if not t:
        return
    p = t
    while p:
        q = p.lc
        if q:
            while q.rc and q.rc != p:
                q = q.rc
            if not q.rc:
                q.rc = p
                p = p.lc
                continue
            else:
                q.rc = None
        print(p.value, end = ' ')
        p = p.rc
    print('')

def morris_pre(t):
    if not t:
        return
    p = t
    while p:
        q = p.lc
        if q:
            while q.rc and q.rc != p:
                q = q.rc
            if not q.rc:
                q.rc = p
                print(p.value, end = ' ')
                p = p.lc
                continue
            else:
                q.rc = None
        else:
            print(p.value, end = ' ')
        p = p.rc
    print('')

def morris_post(t):
    if not t:
        return
    p = t
    while p:
        q = p.lc
        if q:
            while q.rc and q.rc != p:
                q = q.rc
            if not q.rc:
                q.rc = p
                p = p.lc
                continue
            else:
                q.rc = None
                lc = p.lc
                print_right_edge(lc)
        p = p.rc
    print_right_edge(t)
    print('')

def reverse_right_edge(t):
    n = None
    while t:
        q = t
        t = t.rc
        q.rc = n
        n = q
    return n

def print_right_edge(t):
    p = reverse_right_edge(t)
    q = p
    while q:
        print(q.value, end = ' ')
        q = q.rc
    reverse_right_edge(p)

@testwrapper
def test(seq):
    tree = new_bitree_level(seq)
    print_tree(tree)
    morris_pre(tree)
    morris_in(tree)
    morris_post(tree)

def main():
    test([4,2,6,1,3,5,7])
    test([1,2,None,None,3,4,None,None,5])

if __name__ == '__main__':
    main()
