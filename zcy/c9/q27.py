#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def find_kth(a, b, k):
    m = len(a)
    n = len(b)
    if k <= 0 or k > m + n:
        return

    if k <= min(m, n):
        return find_median(a, 0, k-1, b, 0, k-1)
    elif k > max(m, n):
        if a[k-n-1] >= b[-1]:
            return a[k-n-1]
        elif b[k-m-1] >= a[-1]:
            return b[k-m-1]
        else:
            return find_median(a, k-n, m-1, b, k-m, n-1)
    else:
        if m < n:
            t = a
            a = b
            b = t
            t = m
            m = n
            n = t
        if a[k-n-1] >= b[-1]:
            return a[k-n-1]
        else:
            return find_median(a, k-n, k-1, b, 0, n-1)

def find_median(a, sa, ea, b, sb, eb):
    while sa < ea:
        ma = (sa + ea) / 2
        mb = (sb + eb) / 2
        offset = (ea - sa + 1) & 1
        if a[ma] == b[mb]:
            return a[ma]
        elif a[ma] < b[mb]:
            sa = ma + offset
            eb = mb
        else:
            sb = mb + offset
            ea = ma
    return min(a[sa], b[sb])

def test(a, b, k):
    print 'a: {}, b: {}, k: {}'.format(a, b, k)
    print 'kth: {}'.format(find_kth(a, b, k))

def main():
    '''在两个排序数组中找到第K小的数'''
    test([1,2,3,4,5], [3,4,5], 1)
    test([1,2,3], [3,4,5,6], 4)
    test([1,2,3,4,5], [3,4,5], 8)
    test([1,2,3], [3,4,5,6], 8)
    test([1,2,3,4,5], [3,4,5], 4)
    test([1,2,3,4,5], [3,4,5], 7)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
