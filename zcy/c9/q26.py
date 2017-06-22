#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def find_median(a1, a2):
    n = len(a1)
    s1 = s2 = 0
    e1 = e2 = n - 1
    while True:
        if s1 == e1:
            return min(a1[s1], a2[s2])
        else:
            m1 = (s1 + e1) / 2
            m2 = (s2 + e2) / 2
            if a1[m1] == a2[m2]:
                return a1[m1]
            elif a1[m1] < a2[m2]:
                e2 = m2
                if (e1 - s1 + 1) % 2 == 1:
                    s1 = m1
                else:
                    s1 = m1 + 1
            else:
                e1 = m1
                if (e1 - s1 + 1) % 2 == 1:
                    s2 = m2
                else:
                    s2 = m2 + 1

def test(a1, a2):
    print 'a1: {}, a2: {}'.format(a1, a2)
    print 'median: {}'.format(find_median(a1, a2))

def main():
    '''在两个长度相等的排序数组中找到上中位数'''
    test([1,2,3,4], [3,4,5,6])
    test([0,1,2], [3,4,5])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
