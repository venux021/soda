#!/usr/bin/env python3
import math
import sys

from sodacomm.linklist import new_slist, print_list
from sodacomm.tools import testwrapper

def remove_mid(t):
    n = 0
    p = t
    while p:
        n += 1
        p = p.next

    if n == 1:
        return None

    if n % 2 == 0:
        k = n // 2
    else:
        k = n // 2 + 1

    return remove_kth(t, k)

def remove_kth(t, k):
    if k == 1:
        return t.next

    p = t
    i = 1
    while i < k - 1:
        i += 1
        p = p.next

    p.next = p.next.next
    return t

def remove_r(t, r):
    n = 0
    p = t
    while p:
        n += 1
        p = p.next

    k = int(math.ceil(r * n))
    return remove_kth(t, k)

@testwrapper
def test(arr, r):
    slist = new_slist(arr)
    print_list(slist)
    slist = remove_mid(slist)
    print_list(slist)

    slist = new_slist(arr)
    print(r)
    slist = remove_r(slist, r)
    print_list(slist)

def main():
    test([1,2,3,4,5], 0.35)
    test([1,2,3,4,5,6], 0.35)
    test([1], 0.35)
    test([1,2], 0.35)
    test([1,2,3,4,5,6,7,8,9,0], 0.25)

if __name__ == '__main__':
    main()
