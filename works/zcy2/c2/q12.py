#!/usr/bin/env python3
import sys

from sodacomm.linklist import *
from sodacomm.tools import testwrapper

def reverse_each_k(s, k):
    if not s:
        return
    elif k < 1:
        return s

    h = a = Node(next = s)
    b = a
    while True:
        n = 0
        while b and n < k:
            b = b.next
            n += 1
        if not b:
            break
        t = b.next
        b.next = None
        head, tail = reverse_list(a.next)
        a.next = head
        tail.next = t
        a = b = tail
    return h.next

def reverse_list(s):
    p = s
    q = None
    while p:
        t = p
        p = p.next
        t.next = q
        q = t
    return (q, s)

@testwrapper
def test(arr, k):
    slist = new_slist(arr)
    print_list(slist)
    slist = reverse_each_k(slist, k)
    print_list(slist)

def main():
    test([1,2,3,4,5,6,7,8], 3)
    test([1,2,3,4,5,6,7,8], 4)
    test([1,2,3,4], 4)

if __name__ == '__main__':
    main()
