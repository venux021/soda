#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def max_diff(arr):
    n = len(arr)
    LtoR = [0] * n
    RtoL = [0] * n

    mx = LtoR[0] = arr[0]
    for i in range(1,n):
        mx = max(arr[i], mx)
        LtoR[i] = mx

    mx = RtoL[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        mx = max(arr[i], mx)
        RtoL[i] = mx

    mx = 0 - 0x7fffffff
    for i in range(n-1):
        mx = max(mx, abs(LtoR[i] - RtoL[i+1]))

    return mx

def test(arr):
    print 'arr: {}'.format(arr)
    print 'max diff: {}'.format(max_diff(arr))
#    print 'max diff 2: {}'.format(max_diff_2(arr))

def main():
    '''最大的leftMax与rightMax之差的绝对值'''
    test([2,7,3,1,1])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
