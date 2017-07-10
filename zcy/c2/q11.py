#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from linklist import *

def first_intersect(L1, L2):
    c1 = cycle_entry(L1)
    c2 = cycle_entry(L2)
    if (c1 and not c2) or (c2 and not c1):
        return None

    if not c1 and not c2:
        return first_common(L1, L2)

    # L1 and L2 both have cycle
    if c1 == c2:
        return first_common_2(L1, L2, c1)

    i = c1.next
    while i != c1 and i != c2:
        i = i.next

    if i == c1:
        return
    else:
        return c2

def first_common_2(L1, L2, c1):
    len1 = len_until(L1, c1)
    len2 = len_until(L2, c1)
    if len1 > len2:
        long_list = L1
        short_list = L2
    else:
        long_list = L2
        short_list = L1
    k = abs(len1 - len2)

    c = 0
    i = long_list
    while c < k:
        c += 1
        i = i.next

    j = short_list
    while i != j:
        i = i.next
        j = j.next

    return i
    
def len_until(L, node):
    i = 0
    p = L
    while p and p != node:
        i += 1
        p = p.next
    return i

def cycle_entry(L):
    slow = fast = L

    while True:
        if not fast.next or not fast.next.next:
            return
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    fast = L
    while fast != slow:
        fast = fast.next
        slow = slow.next

    return fast

def list_len(L):
    i = 0
    p = L
    while p:
        i += 1
        p = p.next
    return i

def first_common(L1, L2):
    len1 = list_len(L1)
    len2 = list_len(L2)
    if len1 > len2:
        long_list = L1
        short_list = L2
    else:
        long_list = L2
        short_list = L1
    k = abs(len1 - len2)

    i = long_list
    c = 0
    while c < k:
        i = i.next
        c += 1

    j = short_list
    while i and i != j:
        i = i.next
        j = j.next

    return i

def test(s1, s2):
    L1 = parse_list(s1)
    L2 = parse_list(s2)
    fi = first_intersect(L1, L2)
    v = fi.value if fi else None
    print('first intersection:', v)

def find_node(L, value):
    p = L
    while p and p.value != value:
        p = p.next
    return p

def last_node(L):
    p = L
    while p and p.next:
        p = p.next
    return p

def test2(s1, s2, cv):
    L1 = parse_list(s1)
    L2 = parse_list(s2)
    node = find_node(L1, cv)
    last_node(L2).next = node

    fi = first_intersect(L1, L2)
    v = fi.value if fi else None
    print('first intersection:', v)

def test3(s1, cv, s2):
    L1 = parse_list(s1)
    L2 = parse_list(s2)
    node = find_node(L1, cv)
    last_node(L1).next = node

    fi = first_intersect(L1, L2)
    v = fi.value if fi else None
    print('first intersection:', v)

def test4(s1, cv1, s2, cv2):
    L1 = parse_list(s1)
    L2 = parse_list(s2)

    last_node(L2).next = find_node(L1, cv2)
    last_node(L1).next = find_node(L1, cv1)

    fi = first_intersect(L1, L2)
    v = fi.value if fi else None
    print('first intersection:', v)

def test5(s1, cv1, s2, cv2):
    L1 = parse_list(s1)
    L2 = parse_list(s2)

    last_node(L1).next = find_node(L1, cv1)
    last_node(L2).next = find_node(L2, cv2)

    fi = first_intersect(L1, L2)
    v = fi.value if fi else None
    print('first intersection:', v)

def main():
    '''两个单链表相交的一系列问题'''
    test('1 2 3 4', '1 2 3 4')
    test2('1 2 3 4 5 6 7 8', 'a b c d e', '5')
    test2('1 2 3 4 5 6 7 8', 'a b c d e', '1')
    test2('1 2 3 4 5 6 7 8', 'a b c d e', '8')
    test3('1 2 3 4 5 6 7 8 9 0', '4', 'a b c d e f g')
    test4('1 2 3 4 5 6 7 8 9 0', '4', 'a b c d e f g', '3')
    test4('1 2 3 4 5 6 7 8 9 0', '4', 'a b c d e f g', '7')
    test4('1 2 3 4 5 6 7 8 9 0', '4', 'a b c d e f g', '4')
    test5('1 2 3 4 5 6 7', '3', 'a b c d e f g', 'e')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
