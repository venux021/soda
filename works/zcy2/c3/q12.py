#!/usr/bin/env python3
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def build_next(match):
    inext = [None] * len(match)
    nextval = [-1] * len(match)
    inext[0] = nextval[0] = -1
    for i in range(1, len(match)):
        j = inext[i-1]
        while j > -1 and match[j] != match[i-1]:
            j = inext[j]
        inext[i] = j + 1
        if match[i] != match[j+1]:
            nextval[i] = j + 1
        else:
            nextval[i] = nextval[j+1]
        #if match[i] != match[j+1]:
        #    inext[i] = j + 1
        #else:
        #    inext[i] = inext[j+1]
#    return inext
    return nextval

def kmp_match(text, match):
    nextval = build_next(match)
    i = j = 0
    while i < len(text) and j < len(match):
        if j == -1 or text[i] == match[j]:
            i += 1
            j += 1
        else:
            j = nextval[j]
    if j == len(match):
        return i - len(match)
    else:
        return -1

def serial_pre_order(t):
    buf = []
    do_serial(t, buf)
    return ''.join(buf)

def do_serial(t, buf):
    if not t:
        buf.append('#!')
        return
    buf.append(f'{t.value}!')
    do_serial(t.lc, buf)
    do_serial(t.rc, buf)

def has_sub_tree_by_topo(t1, t2):
    s1 = serial_pre_order(t1)
    s2 = serial_pre_order(t2)
    return kmp_match(s1, s2) > -1

@testwrapper
def test(s1, s2):
    t1 = new_bitree_level(s1)
    t2 = new_bitree_level(s2)
    print_tree(t1)
    print_tree(t2)
    print(has_sub_tree_by_topo(t1, t2))

def main():
    test([1,2,3,4,5,6,7,None,8,9], [2,4,5,None,8,9])
    test([1,2,3,4,5,6,7,None,8,9], [2,4,5,None,8])

if __name__ == '__main__':
    main()
