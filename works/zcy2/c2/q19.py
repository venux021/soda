#!/usr/bin/env python3
import sys

from sodacomm.linklist import *
from sodacomm.tools import testwrapper

def merge_s(s1, s2):
    p1 = s1
    p2 = s2
    head = tail = None
    while p1 and p2:
        if p1.value < p2.value:
            t = p1
            p1 = p1.next
            if not head:
                head = tail = t
            else:
                tail.next = t
                tail = t
        else:
            t = p2
            p2 = p2.next
            if not head:
                head = tail = t
            else:
                tail.next = t
                tail = t
    p = p1 or p2
    if p:
        tail.next = p
    return head

def merge_s2(s1, s2):
    if s1.value < s2.value:
        p = s1
        q = s2
    else:
        p = s2
        q = s1
    head = p
    while p.next and q:
        if p.next.value <= q.value:
            p = p.next
        else:
            t = q
            q = q.next
            t.next = p.next
            p.next = t
    if q:
        p.next = q
    return head

@testwrapper
def test(a1, a2):
    s1 = new_slist(a1)
    s2 = new_slist(a2)
    print_list(s1)
    print_list(s2)
    s = merge_s(s1, s2)
    print_list(s)

    s1 = new_slist(a1)
    s2 = new_slist(a2)
    print_list(s1)
    print_list(s2)
    s = merge_s2(s1, s2)
    print_list(s)

def main():
    test([1,3,5,7,9], [2,4,6,8,10])
    test([1,3,5,7,9], [2,4])
    test([1,2,3,4], [5,6,7,8])

if __name__ == '__main__':
    main()
