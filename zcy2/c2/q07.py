#!/usr/bin/env python3
import sys

from sodacomm.linklist import *
from sodacomm.tools import testwrapper

def is_palindrome(slist):
    if not slist or not slist.next:
        return True
    p = q = slist
    while p.next and p.next.next:
        p = p.next.next
        q = q.next

    px = slist
    y = reverse_slist(q.next)
    py = y
    while py and py.value == px.value:
        py = py.next
        px = px.next
    reverse_slist(y)
    return not py

def reverse_slist(slist):
    p = slist
    q = None
    while p:
        t = p
        p = p.next
        t.next = q
        q = t
    return q

@testwrapper
def test(arr):
    slist = new_slist(arr)
    print_list(slist)
    print(is_palindrome(slist))

def main():
    test([1,2,2,1])
    test([1,2,1])
    test([1,2])
    test([1,1])
    test([1])
    test([1,2,3])

if __name__ == '__main__':
    main()
