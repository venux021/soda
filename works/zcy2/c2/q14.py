#!/usr/bin/env python3
import sys

from sodacomm.linklist import *
from sodacomm.tools import testwrapper

def remove_by_value(h, num):
    if not h.next:
        return
    s = h.next
    head = tail = None
    p = s
    while p:
        t = p
        p = p.next
        if t.value != num:
            if not head:
                head = tail = t
            else:
                tail.next = t
                tail = t
    h.next = head
    return h

@testwrapper
def test(arr, num):
    h = new_slist_h(arr)
    print_list(h.next)
    h = remove_by_value(h, num)
    print_list(h.next)

def main():
    test([1,2,3,4], 3)
    test([1,2], 1)
    test([1], 1)

if __name__ == '__main__':
    main()
