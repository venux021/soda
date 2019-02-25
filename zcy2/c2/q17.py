#!/usr/bin/env python3
import sys

from sodacomm.linklist import *
from sodacomm.tools import testwrapper

def remove_node(n):
    if not n or not n.next:
        return
    t = n.next
    n.value = t.value
    n.next = t.next

@testwrapper
def test(arr, k):
    s = new_slist(arr)
    n = find_first(s, k)
    print_list(s)
    remove_node(n)
    print_list(s)

def main():
    test([1,2,3], 2)
    test([1,2,3], 1)
    test([1,2,3], 3)

if __name__ == '__main__':
    main()
