#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def extern_sort_with_loser_tree(*arrs):
    n = len(arrs)
    for a in arrs:
        a.append(sys.maxsize)
    arrs = list(arrs)
    arrs.append([-sys.maxsize])
    ptrs = [0] * (n+1)
    tree = [n] * n

    for i in range(n):
        adjust(tree, n, arrs, ptrs, i)

    while True:
        win = tree[0]
        value = arrs[win][ptrs[win]]
        if value >= sys.maxsize:
            break
        yield value
        load(arrs, ptrs, win)
        adjust(tree, n, arrs, ptrs, win)

def load(arrs, ptrs, i):
    if arrs[i][ptrs[i]] < sys.maxsize:
        ptrs[i] += 1

def adjust(tree, k, arrs, ptrs, i):
    t = (i + k) // 2
    chall = i
    while t > 0:
        if arrs[chall][ptrs[chall]] > arrs[tree[t]][ptrs[tree[t]]]:
            tree[t], chall = chall, tree[t]
        t //= 2
    tree[0] = chall

@testwrapper
def test(*arrs):
    for a in arrs:
        print(a)
    for value in extern_sort_with_loser_tree(*arrs):
        print(value, end = ' ')
    print('')

def main():
    test([1,3,5,7,9], [2,4,9,13,24], [1,2,3,4,5,6,7,8,9,10], [-3,-2,-1,2,9,13], [-1,3,6,11,17,25,33,40])

if __name__ == '__main__':
    main()
