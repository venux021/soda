#!/usr/bin/env python3
from collections import deque
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

class Rec:

    def __init__(self, left = 0, right = 0):
        self.left = left
        self.right = right

    @property
    def total(self):
        return self.left + self.right + 1

def max_topo2(t):
    biggest = [0]
    do_max_topo2(t, biggest)
    return biggest[0]

def do_max_topo2(t, biggest):
    if t.lc and t.lc.value < t.value:
        do_max_topo2(t.lc, biggest)
        lc = t.lc
        p = lc
        while p and p.value < t.value:
            p = p.rc
        if p:
            q = lc
            while q != p:
                q.rec.right -= p.rec.total
                q = q.rc
        left = t.lc.rec.total
    else:
        left = 0
    if t.rc and t.rc.value > t.value:
        do_max_topo2(t.rc, biggest)
        rc = t.rc
        p = rc
        while p and p.value > t.value:
            p = p.lc
        if p:
            q = rc
            while q != p:
                q.rec.left -= p.rec.total
                q = q.lc
        right = t.rc.rec.total
    else:
        right = 0
    t.rec = Rec(left = left, right = right)
    if t.rec.total > biggest[0]:
        biggest[0] = t.rec.total

def max_topo(t):
    if not t:
        return 0
    L = max_topo(t.lc)
    R = max_topo(t.rc)
    S = 0
    qu = deque([t])
    while qu:
        f = qu.popleft()
        if bfind(t, f):
            S += 1
            if f.lc:
                qu.append(f.lc)
            if f.rc:
                qu.append(f.rc)
    return max(L, R, S)

def bfind(t, f):
    p = t
    while p:
        if f.value < p.value:
            p = p.lc
        elif f.value > p.value:
            p = p.rc
        else:
            return True
    return False

@testwrapper
def test(seq):
    tree = new_bitree_level(seq)
    print_tree(tree)
    print(max_topo(tree))
    print(max_topo2(tree))

def main():
    test([6,1,12,0,3,10,13,None,None,None,None,4,14,20,16,2,5,11,15])

if __name__ == '__main__':
    main()
