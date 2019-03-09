#!/usr/bin/env python3
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def longest_path(t, num):
    sum_map = {0: 0}
    longest = [0]
    do_find(t, 0, 0, num, sum_map, longest)
    return longest[0]

def do_find(t, level, cur_sum, num, sum_map, longest):
    if not t:
        return
    v = cur_sum + t.value
    if v not in sum_map:
        sum_map[v] = level + 1

    k = v - num
    if k in sum_map:
        length = sum_map[v] - sum_map[k]
    else:
        length = 0

    if length > longest[0]:
        longest[0] = length
    do_find(t.lc, level + 1, v, num, sum_map, longest)
    do_find(t.rc, level + 1, v, num, sum_map, longest)
    if sum_map[v] == level + 1:
        del sum_map[v]

@testwrapper
def test(arr, num):
    tree = new_bitree_level(arr)
    print_tree(tree)
    print(num)
    print(longest_path(tree, num))

def main():
    test([-3,3,-9,1,0,2,1,None,None,1,6], 6)
    test([-3,3,-9,1,0,2,1,None,None,1,6], -9)

if __name__ == '__main__':
    main()
