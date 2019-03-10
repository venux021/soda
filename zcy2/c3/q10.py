#!/usr/bin/env python3
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def find_err(t):
    err = [None, None]
    last = [None]
    do_find(t, err, last)
    if not any(err):
        return t
    else:
        print(f'{err[0].value} <-> {err[1].value}')
        return exchange(t, err[0], err[1])

def exchange(t, e1, e2):
    p1, p2 = find_parent(t, e1, e2)
    if e1 == t or e2 == t:
        if e2 == t:
            e1, e2 = e2, e1
            p1, p2 = p2, p1
        e2L, e2R = e2.lc, e2.rc
        if e1.lc == e2:
            e2.lc = e1
            e2.rc = e1.rc
            e1.lc, e1.rc = e2L, e2R
        elif e1.rc == e2:
            e2.lc = e1.lc
            e2.rc = e1
            e1.lc, e1.rc = e2L, e2R
        elif p2.lc == e2:
            p2.lc = e1
            e2.lc, e2.rc = e1.lc, e1.rc
            e1.lc, e1.rc = e2L, e2R
        else:
            p2.rc = e1
            e2.lc, e2.rc = e1.lc, e1.rc
            e1.lc, e1.rc = e2L, e2R
        return e2
    elif e1.lc == e2 or e1.rc == e2 or e2.lc == e1 or e2.rc == e1:
        if e2.lc == e1 or e2.rc == e1:
            e2, e1 = e1, e2
            p2, p1 = p1, p2
        e2L, e2R = e2.lc, e2.rc
        if p1.lc == e1:
            p1.lc = e2
        else:
            p1.rc = e2
        if e1.lc == e2:
            e2.lc = e1
            e2.rc = e1.rc
        else:
            e2.lc = e1.lc
            e2.rc = e1
        e1.lc, e1.rc = e2L, e2R
        return t
    elif p1 == p2:
        e2L, e2R = e2.lc, e2.rc
        e2.lc, e2.rc = e1.lc, e1.rc
        e1.lc, e1.rc = e2L, e2R
        p1.lc, p1.rc = p1.rc, p1.lc
        return t
    else:
        e1L, e1R = e1.lc, e1.rc
        e2L, e2R = e2.lc, e2.rc
        if p1.lc == e1:
            p1.lc = e2
        else:
            p1.rc = e2
        if p2.lc == e2:
            p2.lc = e1
        else:
            p2.rc = e1
        e1.lc, e1.rc = e2L, e2R
        e2.lc, e2.rc = e1L, e1R
        return t

def find_parent(t, e1, e2):
    parents = [None, None]
    do_find_p(t, e1, e2, parents)
    return parents

def do_find_p(t, e1, e2, parents):
    if not t:
        return False
    if t.lc == e1 or t.rc == e1:
        parents[0] = t
    if t.lc == e2 or t.rc == e2:
        parents[1] = t
    if all(parents):
        return True
    return do_find_p(t.lc, e1, e2, parents) or do_find_p(t.rc, e1, e2, parents)

def do_find(t, err, last):
    if not t:
        return False
    if do_find(t.lc, err, last):
        return True
    if last[0] and last[0].value > t.value:
        err[1] = t
        if not err[0]:
            err[0] = last[0]
        else:
            return True
    last[0] = t
    return do_find(t.rc, err, last)

@testwrapper
def test(seq):
    tree = new_bitree_level(seq)
    print_tree(tree)
    tree = find_err(tree)
    print_tree(tree)

def main():
    test([4,2,5,1,3,None,6])
    test([4,2,5,3,1,None,6])
    test([4,5,2,1,3,None,6])
    test([4,2,6,1,3,None,5])
    test([4,1,5,2,3,None,6])
    test([4,2,5,1,3,None,6])
    test([5,2,4,1,3,None,6])
    test([2,4,5,1,3,None,6])
    test([3,2,5,1,4,None,6])
    test([4,2,3,1,5,None,6])

if __name__ == '__main__':
    main()
