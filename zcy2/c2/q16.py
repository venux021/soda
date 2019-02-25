#!/usr/bin/env python3
import sys

from sodacomm.linklist import *
from sodacomm.tools import testwrapper

def slist_select_sort(s):
    if not s:
        return
    head = tail = None
    t = Node(next = s)
    while t.next:
        min_v = t.next.value
        p_v = t
        p = t
        while p.next:
            if p.next.value < min_v:
                min_v = p.next.value
                p_v = p
            p = p.next
        n = p_v.next
        p_v.next = n.next
        if not head:
            head = tail = n
        else:
            tail.next = n
            tail = n
    return head

@testwrapper
def test(arr):
    s = new_slist(arr)
    print_list(s)
    s = slist_select_sort(s)
    print_list(s)

def main():
    test([1])
    test([1,2])
    test([2,1])
    test([7,3,1,5,2,6,9,0])

if __name__ == '__main__':
    main()
