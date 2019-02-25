#!/usr/bin/env python3
import sys

from sodacomm.linklist import *
from sodacomm.tools import testwrapper

def insert_loop(s, num):
    if not s:
        n = Node(num)
        n.next = n
        return n
    if s.next == s:
        n = Node(num)
        s.next = n
        n.next = s
        if num >= s.value:
            return s
        else:
            return n

    if num < s.value:
        n = Node(num)
        n.next = s
        get_loop_tail(s).next = n
        return n

    p = s
    while p.next != s and p.next.value < num:
        p = p.next

    n = Node(num)
    n.next = p.next
    p.next = n
    return s

def get_loop_tail(s):
    p = s
    while p.next != s:
        p = p.next
    return p

def print_loop(s):
    if not s:
        return
    if s.next == s:
        print(s.value)
        return
    p = s
    while p.next != s:
        print(p.value, end = ' ')
        p = p.next
    print(p.value, end = ' ')
    print('')

@testwrapper
def test(arr, num):
    s = new_slist(arr)
    get_tail(s).next = s
    print_loop(s)
    s = insert_loop(s, num)
    print_loop(s)

def main():
    test([1,2,3,4,5], 0)
    test([1,2,3,4,5], 1)
    test([1,2,3,4,5], 3)
    test([1,2,3,4,5], 5)
    test([1,2,3,4,5], 6)
    test([1], 2)
    test([1], 0)

if __name__ == '__main__':
    main()
