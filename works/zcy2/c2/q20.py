#!/usr/bin/env python3
import sys

from sodacomm.linklist import *
from sodacomm.tools import testwrapper

def trans(s):
    n = get_length(s)
    if n == 1:
        return s
    half = n // 2
    p = s
    k = 1
    while k < half:
        p = p.next
        k += 1
    p1 = s
    p2 = p.next
    p.next = None
    head = tail = None
    while p1 and p2:
        t = p1
        p1 = p1.next
        if not head:
            head = tail = t
        else:
            tail.next = t
            tail = t
        t = p2
        p2 = p2.next
        tail.next = t
        tail = t
    tail.next = p2
    return head

def get_length(s):
    n = 0
    p = s
    while p:
        n += 1
        p = p.next
    return n

@testwrapper
def test(arr):
    s = new_slist(arr)
    print_list(s)
    s = trans(s)
    print_list(s)

def main():
    test([1])
    test([1,2])
    test([1,2,3])
    test([1,2,3,4])
    test([1,2,3,4,5])
    test([1,2,3,4,5,6])

if __name__ == '__main__':
    main()
