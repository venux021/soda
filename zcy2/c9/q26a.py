#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def kth_element(a1, a2, k):
    n1 = len(a1)
    n2 = len(a2)
    if k < 0 or k > n1 + n2:
        return
    if n1 > n2:
        short, short_size = a2, n2
        Long, Long_size = a1, n1
    else:
        short, short_size = a1, n1
        Long, Long_size = a2, n2

    if k <= short_size:
        return upper_median(short[:k], Long[:k])
    elif k > Long_size:
        if short[k-Long_size-1] >= Long[-1]:
            return short[k-Long_size-1]
        elif Long[k-short_size-1] >= short[-1]:
            return Long[k-short_size-1]
        else:
            return upper_median(short[k-Long_size:], Long[k-short_size:])
    else:
        if Long[k-short_size-1] >= short[-1]:
            return Long[k-short_size-1]
        else:
            lower = k - short_size
            upper = k
            return upper_median(short, Long[lower:upper])

def upper_median(a1, a2):
    n = len(a1)
    b1, e1 = 0, n-1
    b2, e2 = 0, n-1
    while b1 < e1:
        m1 = (b1 + e1) // 2
        m2 = (b2 + e2) // 2
        offset = 1 - ((e1 - b1 + 1) & 1)
        if a1[m1] == a2[m2]:
            return a1[m1]
        elif a1[m1] > a2[m2]:
            e1 = m1
            b2 = m2 + offset
        else:
            e2 = m2
            b1 = m1 + offset
    return min(a1[b1], a2[b2])

@testwrapper
def test(a1, a2, k):
    print(a1, a2, k)
    print(kth_element(a1, a2, k))

def main():
#    test([1,2,3,4,5], [3,4,5], 1)
#    test([1,2,3,4,5], [3,4,5], 2)
#    test([1,2,3,4,5], [3,4,5], 3)
#    test([1,2,3], [3,4,5,6], 4)
#    test([1,2,3], [3,4,5,6], 6)
#    test([1,2,3], [3,4,5,6], 7)
#    test([1,2,6], [3,4,5,10], 6)
#    test([1,2,6], [3,4,5,10], 5)
    test([1,2], [1,2,3], 3)

if __name__ == '__main__':
    main()
