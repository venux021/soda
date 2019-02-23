#!/usr/bin/env python3
import sys

from sodacomm.linklist import *
from sodacomm.tools import testwrapper

def get_intersect(s1, s2):
    if not s1 or not s2:
        return
    p1 = find_loop(s1)
    p2 = find_loop(s2)

    if not p1 and not p2:
        return get_intersect_without_loop(s1, s2)
    elif p1 and p2:
        if p1 == p2:
            return get_intersect_before_loop(s1, s2, p1)
        else:
            q = p1.next
            while q != p1 and q != p2:
                q = q.next
            if q == p2:
                return p2
            else:
                return

def get_intersect_before_loop(s1, s2, p1):
    def _get_length(s):
        n = 1
        p = s
        while p != p1:
            p = p.next
            n += 1
        return (n, p)
    n1, t1 = _get_length(s1)
    n2, t2 = _get_length(s2)
    p1 = s1
    p2 = s2
    if n1 > n2:
        for i in range(n1-n2):
            p1 = p1.next
    elif n1 < n2:
        for i in range(n2-n1):
            p2 = p2.next
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1

def find_loop(s):
    if not s.next:
        return 
    elif s.next == s:
        return s
    slow = s.next
    fast = s.next.next
    while fast != slow:
        slow = slow.next
        if not fast.next or not fast.next.next:
            return
        fast = fast.next.next
    fast = s
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

def get_intersect_without_loop(s1, s2):
    n1, t1 = get_length(s1)
    n2, t2 = get_length(s2)
    if t1 != t2:
        return
    p1 = s1
    p2 = s2
    if n1 > n2:
        for i in range(n1-n2):
            p1 = p1.next
    elif n1 < n2:
        for i in range(n2-n1):
            p2 = p2.next
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1

def get_length(s):
    n = 1
    p = s
    while p.next:
        p = p.next
        n += 1
    return (n, p)

def dotest(s1, s2):
    i = get_intersect(s1, s2)
    if i:
        print(i.value)
    else:
        print(None)

@testwrapper
def test_1():
    s1 = new_slist([1,2,3,4,5])
    s2 = new_slist([2,3,4,5,6])
    print_list(s1)
    print_list(s2)
    dotest(s1, s2)

@testwrapper
def test_2():
    s1 = new_slist([1,2,3,4,5])
    s2 = new_slist([2,3,4,5,6])
    print_list(s1)
    print_list(s2)
    get_tail(s2).next = find_first(s1, 3)
    dotest(s1, s2)

@testwrapper
def test_3():
    s1 = new_slist([1,2,3,4,5])
    s2 = new_slist([2,3,4,5,6])
    get_tail(s1).next = find_first(s1, 2)
    get_tail(s2).next = find_first(s2, 4)
    dotest(s1, s2)

@testwrapper
def test_4():
    s1 = new_slist([1,2,3,4,5])
    s2 = new_slist([2,3,4,5,6])
    get_tail(s2).next = find_first(s1, 4)
    get_tail(s1).next = find_first(s1, 2)
    dotest(s1, s2)

@testwrapper
def test_5():
    s1 = new_slist([1,2,3,4,5])
    s2 = new_slist([2,3,4,5,6])
    get_tail(s2).next = find_first(s1, 2)
    get_tail(s1).next = find_first(s1, 3)
    dotest(s1, s2)

def main():
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()

if __name__ == '__main__':
    main()
