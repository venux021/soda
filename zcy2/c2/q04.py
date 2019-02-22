#!/usr/bin/env python3
import sys

from sodacomm.linklist import *
from sodacomm.tools import testwrapper

def reverse_s(slist):
    q = None
    p = slist
    while p:
        t = p
        p = p.next
        t.next = q
        q = t
    return q

def reverse_d(dlist):
    q = None
    p = dlist
    while p:
        t = p
        p = p.next
        t.next = q
        if q:
            q.prev = t
        q = t
    q.prev = None
    return q

@testwrapper
def test(arr):
    slist = new_slist(arr)
    print_list(slist)
    slist = reverse_s(slist)
    print_list(slist)

    dlist = new_dlist(arr)
    print_list(dlist)
    dlist = reverse_d(dlist)
    print_list(dlist)

def main():
    test([1])
    test([1,2,3,4,5])

if __name__ == '__main__':
    main()
