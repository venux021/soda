#!/usr/bin/env python3
import sys

from sodacomm.linklist import *
from sodacomm.tools import testwrapper

def remove_dup_1(s):
    if not s:
        return
    m = set()
    head = tail = None
    p = s
    while p:
        t = p
        p = p.next
        if t.value in m:
            continue
        m.add(t.value)
        if not head:
            head = tail = t
        else:
            tail.next = t
            tail = t
    tail.next = None
    return head

def remove_dup_2(s):
    if not s:
        return
    _h = Node(next = s)
    head = tail = None
    while _h.next:
        n = _h.next
        _h.next = n.next
        n.next = None
        if not head:
            head = tail = n
        else:
            tail.next = n
            tail = n
        v = n.value
        p = _h
        while p.next:
            if p.next.value == v:
                t = p.next
                p.next = t.next
            else:
                p = p.next
    return head

@testwrapper
def test(arr):
    s = new_slist(arr)
    print_list(s)
    print_list(remove_dup_1(s))
    s = new_slist(arr)
    print_list(remove_dup_2(s))

def main():
    test([1,2,3,3,4,4,2,1,1])
    test([1,2,3,4])
    test([1,1,1,1])

if __name__ == '__main__':
    main()
