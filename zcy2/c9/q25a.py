#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def find_up_median(a1, a2):
    n = len(a1)
    assert n > 0 and n == len(a2)

    b1, e1 = 0, n-1
    b2, e2 = 0, n-1
    while b1 != e1:
        m1 = (b1 + e1) // 2
        m2 = (b2 + e2) // 2
        if a1[m1] == a2[m2]:
            return a1[m1]
        elif a1[m1] > a2[m2]:
            e1 = m1
            b2 = m2 + ((b2-e2) & 1)
        else:
            b1 = m1 + ((b1-e1) & 1)
            e2 = m2
    return min(a1[b1], a2[b2])

@testwrapper
def test(a1, a2):
    print(a1, a2)
    print(find_up_median(a1, a2))

def main():
    test([1,2,3,4], [3,4,5,6])
    test([0,1,2], [3,4,5])
    test([1,10], [2,9])
    test([1,10], [0,19])

if __name__ == '__main__':
    main()
