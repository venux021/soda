#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def sort_with_stack(stk):
    k = []
    while stk:
        t = stk.pop()
        while k and k[-1] < t:
            stk.append(k.pop())
        k.append(t)
    while k:
        stk.append(k.pop())

@testwrapper
def test(arr):
    stk = arr[:]
    print(stk)
    sort_with_stack(stk)
    print(stk)

def main():
    test([4,7,2,8,10])
    test([5,2,1,-3,7,-10,7])

if __name__ == '__main__':
    main()
