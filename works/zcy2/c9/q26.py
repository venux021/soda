#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def upper_median(a, b):
    assert len(a) == len(b)
    n = len(a)
    a1, a2 = 0, n-1
    b1, b2 = 0, n-1
    while a1 < a2:
        ma = (a1 + a2) // 2
        mb = (b1 + b2) // 2
        offset = ((a2 - a1 + 1) & 1) ^ 1
        if a[ma] < b[mb]:
            a1 = ma + offset
            b2 = mb
        elif a[ma] > b[mb]:
            a2 = ma
            b1 = mb + offset
        else:
            return a[ma]
    return min(a[a1], b[b1])

def kth_element(a, b, k):
    na = len(a)
    nb = len(b)
    if na < nb:
        ns, nL = na, nb
        rs, rL = a, b
    else:
        ns, nL = nb, na
        rs, rL = b, a

    if k < 1 or k > (na + nb):
        return
    elif k <= ns:
        return upper_median(a[:k], b[:k])
    elif k > nL:
        if rs[k-nL-1] > rL[-1]:
            return rs[k-nL-1]
        elif rL[k-ns-1] > rs[-1]:
            return rL[k-ns-1]
        else:
            return upper_median(rs[k-nL:], rL[k-ns:])
    elif rL[k-ns-1] >= rs[-1]:
        return rL[k-ns-1]
    else:
        return upper_median(rs, rL[k-ns:k])

@testwrapper
def test(a, b, k):
    print(a, b, k)
    print(kth_element(a, b, k))

def main():
    test([1,2,3,4,5], [3,4,5], 1)
    test([1,2,3], [3,4,5,6], 4)
    test([1,2,3], [3,4,5,6], 6)
    test([1,2,3], [3,4,5,6], 7)
    test([1,2,6], [3,4,5,10], 6)
    test([1,2,6], [3,4,5,10], 5)

if __name__ == '__main__':
    main()
