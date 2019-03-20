#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def find_left_most(strs, s):
    if s is None:
        return -1
    n = len(strs)
    L, R = 0, n - 1
    res = -1
    while L <= R:
        mid = (L+R) // 2
        if strs[mid] == s:
            res = mid
            R = mid - 1
        elif strs[mid] and s < strs[mid]:
            R = mid - 1
        elif strs[mid] and s > strs[mid]:
            L = mid + 1
        else:
            i = mid - 1
            while i >= L and strs[i] is None:
                i -= 1
            if i < L:
                L = mid + 1
            elif strs[i] >= s:
                if strs[i] == s:
                    res = i
                R = i - 1 
            else:
                L = i + 1
    return res

@testwrapper
def test(strs, s):
    print(strs, s)
    print(find_left_most(strs, s))

def main():
    test([None,'a',None,'a',None,'b',None,'c'], 'a')
    test([None,'a',None,'a',None,'b',None,'c'], 'b')
    test([None,'a',None,'a',None,'b',None,'c'], None)
    test([None,'a',None,'a',None,'b',None,'c'], 'd')

if __name__ == '__main__':
    main()
