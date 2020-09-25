#!/usr/bin/env python3
import sys

from sodacomm.linklist import *
from sodacomm.tools import testwrapper

def sadd(s1, s2):
    if not s1:
        return s2
    elif not s2:
        return s1

    s1 = reverse(s1)
    s2 = reverse(s2)

    p1 = s1
    p2 = s2
    head = tail = None
    carry = 0
    while p1 and p2:
        v = p1.value + p2.value + carry
        carry = 0
        if v >= 10:
            carry = 1
            v -= 10
        node = Node(v)
        if not head:
            head = tail = node
        else:
            tail.next = node
            tail = node
        p1 = p1.next
        p2 = p2.next
    px = p1 or p2
    while px:
        v = px.value + carry
        carry = 0
        if v >= 10:
            carry = 1
            v -= 10
        node = Node(v)
        tail.next = node
        tail = node
        px = px.next
    if carry == 1:
        node = Node(1)
        tail.next = node
    return reverse(head)

def reverse(s):
    p = s
    q = None
    while p:
        t = p
        p = t.next
        t.next = q
        q = t
    return q

@testwrapper
def test(a1, a2):
    s1 = new_slist(a1)
    s2 = new_slist(a2)
    print_list(s1)
    print_list(s2)
    k = sadd(s1, s2)
    print_list(k)

def main():
    test([9,3,7], [6,3])
    test([9,9,9], [2])

if __name__ == '__main__':
    main()
