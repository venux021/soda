#!/usr/bin/env python3
import sys

from sodacomm.linklist import *
from sodacomm.tools import testwrapper

def reverse_section(slist, a, b):
    if a < 1 or b < 1 or a == b:
        return slist
    if a > b:
        a, b = b, a
    head = Node(next = slist)
    p = slist
    i = 1
    while p and i < b-a:
        p = p.next
        i += 1
    if not p:
        return slist
    q = head
    while p and i < b-1:
        p = p.next
        q = q.next
        i += 1
    p = p.next
    t1 = q
    h2 = p.next
    p.next = None

    x = q.next
    z = h2
    while x:
        y = x
        x = x.next
        y.next = z
        z = y
    t1.next = z

    return head.next

@testwrapper
def test(arr, a, b):
    slist = new_slist(arr)
    print_list(slist)
    slist = reverse_section(slist, a, b)
    print_list(slist)

def main():
    test([1,2,3,4,5], 2, 4)
    test([1,2,3,4,5], 2, 3)
    test([1,2,3,4,5], 1, 3)
    test([1,2,3,4,5], 1, 5)
    test([1,2,3,4,5], 4, 5)

if __name__ == '__main__':
    main()
