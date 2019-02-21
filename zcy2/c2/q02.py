#!/usr/bin/env python3
import sys

from sodacomm.linklist import new_slist, new_dlist, print_list
from sodacomm.tools import testwrapper

def remove_last_kth_s(slist, k):
    n = 0
    p = slist
    while p:
        n += 1
        p = p.next
    if k > n:
        return slist
    elif k == n:
        r = slist.next
        slist.next = None
        return r
    else:
        i = 1
        p = slist
        while i < n-k:
            p = p.next
            i += 1
        q = p.next
        p.next = q.next
        return slist

def remove_last_kth_d(dlist, k):
    p = dlist
    i = 1
    while i < k and p:
        p = p.next
        i += 1
    if not p:
        return dlist

    j = dlist
    while p.next:
        p = p.next
        j = j.next

    if j == dlist:
        j.next.prev = None
        return j.next

    x = j.prev
    x.next = j.next
    y = j.next
    if y:
        y.prev = x
    return dlist

@testwrapper
def test(arr, k):
    print(k)
    slist = new_slist(arr)
    print_list(slist)
    slist = remove_last_kth_s(slist, k)
    print_list(slist)

    dlist = new_dlist(arr)
    print_list(dlist)
    dlist = remove_last_kth_d(dlist, k)
    print_list(dlist)

def main():
    test([1,2,3,4,5], 3)
    test([1,2,3,4,5], 1)
    test([1,2,3,4,5], 5)
    test([1,2,3,4,5], 6)

if __name__ == '__main__':
    main()
