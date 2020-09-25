#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def longest(arr):
    L = 0
    m = {}
    for j in range(len(arr)):
        i = arr[j]
        if i not in m:
            m[i] = 1
            if i-1 in m:
                A = m[i-1]
                left_a = i-1 - m[i-1] + 1
                right_a = i
                len_a = m[i] + m[i-1]
                L = max(L, len_a)
                m[left_a] = m[right_a] = len_a
            if i+1 in m:
                B = m[i+1]
                left_b = i - m[i] + 1
                right_b = i+1 + B - 1
                len_b = m[i] + m[i+1]
                L = max(L, len_b)
                m[left_b] = m[right_b] = len_b
    return L

def test(arr):
    print 'arr: {}'.format(arr)
    print 'max: {}'.format(longest(arr))

def main():
    '''数组中的最长连续序列'''
    test([100,4,200,1,3,2])
    test([9,10,4,12,1,11,3,8,2])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
