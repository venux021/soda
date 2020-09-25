#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def find_upper_median(a1, a2):
    assert len(a1) == len(a2)
    n = len(a1)
    a1b, a1e = 0, n-1
    a2b, a2e = 0, n-1
    while a1b < a1e:
        m1 = (a1b + a1e) // 2
        m2 = (a2b + a2e) // 2
        if a1[m1] <= a2[m2]:
            if (a1e - a1b + 1) % 2 == 1:
                a1b = m1
            else:
                a1b = m1 + 1
            a2e = m2
        else:
            if (a1e - a1b + 1) % 2 == 1:
                a2b = m2
            else:
                a2b = m2 + 1
            a1e = m1
    return min(a1[a1b], a2[a2b])

@testwrapper
def test(a1, a2):
    print(a1, a2)
    print(find_upper_median(a1, a2))

def main():
    test([1,2,3,4], [3,4,5,6])
    test([0,1,2], [3,4,5])
    test([1,10], [2,9])
    test([1,10], [0,19])

if __name__ == '__main__':
    main()
