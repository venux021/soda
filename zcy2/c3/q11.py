#!/usr/bin/env python3
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def is_contain(t1, t2):
    if not all((t1, t2)):
        return False
    if not t1 and not t2:
        return True

    if t1.value == t2.value and docomp(t1, t2):
        return True

    return is_contain(t1.lc, t2) or is_contain(t1.rc, t2)

def docomp(t1, t2):
    if not t2:
        return True
    elif not t1:
        return False
    elif t1.value != t2.value:
        return False
    else:
        return docomp(t1.lc, t2.lc) and docomp(t1.rc, t2.rc)

@testwrapper
def test(s1, s2):
    t1 = new_bitree_level(s1)
    t2 = new_bitree_level(s2)
    print_tree(t1)
    print_tree(t2)
    print(is_contain(t1, t2))

def main():
    test([1,2,3,4,5,6,7,8,9,10], [2,4,5,8])

if __name__ == '__main__':
    main()
