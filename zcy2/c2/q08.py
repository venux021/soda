#!/usr/bin/env python3
import sys

from sodacomm.linklist import *
from sodacomm.tools import testwrapper

def slist_partition(slist, pivot):
    if not slist:
        return None
    shead = stail = None
    ehead = etail = None
    bhead = btail = None
    p = slist
    while p:
        t = p
        p = p.next
        if t.value < pivot:
            if shead is None:
                shead = stail = t
            else:
                stail.next = t
                stail = t
        elif t.value == pivot:
            if ehead is None:
                ehead = etail = t
            else:
                etail.next = t
                etail = t
        else:
            if bhead is None:
                bhead = btail = t
            else:
                btail.next = t
                btail = t
        t.next = None

    if stail:
        if ehead:
            stail.next = ehead
        else:
            stail.next = bhead
    if etail:
        etail.next = bhead
    if shead:
        return shead
    elif ehead:
        return ehead
    else:
        return bhead

@testwrapper
def test(arr, pivot):
    slist = new_slist(arr)
    print_list(slist)
    slist = slist_partition(slist, pivot)
    print(f'pivot: {pivot}')
    print_list(slist)

def main():
    test([7,9,1,8,5,2,5], 5)
    test([9,0,4,5,1], 3)
    test([5,4,3,2,1], 0)
    test([5,4,3,2,1], 1)
    test([5,4,3,2,1], 3)
    test([5,4,3,2,1], 5)
    test([5,4,3,2,1], 6)

if __name__ == '__main__':
    main()
