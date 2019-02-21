#!/usr/bin/env python3
import sys

from sodacomm.linklist import new_slist
from sodacomm.tools import testwrapper

def print_common(t1, t2):
    p1 = t1
    p2 = t2
    while p1 and p2:
        if p1.value < p2.value:
            p1 = p1.next
        elif p1.value > p2.value:
            p2 = p2.next
        else:
            print(p1.value, end = ' ')
            p1 = p1.next
            p2 = p2.next
    print('')

@testwrapper
def test(a1, a2):
    t1 = new_slist(a1)
    t2 = new_slist(a2)
    print_common(t1, t2)

def main():
    test([1,3,5,7,9], [1,2,3,4,5,6,7,8,9])
    test([1,2,3,4,5], [3,4,5,6,7])
    test([1], [2])

if __name__ == '__main__':
    main()
