#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from collections import deque

def win_max(arr, k):
    mxq = deque()
    r = []
    for i in range(len(arr)):
        if mxq and i - mxq[0] >= k:
            mxq.popleft()

        while mxq and arr[i] > arr[mxq[-1]]:
            mxq.pop()
        mxq.append(i)

        if i >= k-1:
            r.append(arr[mxq[0]])
    return r

def test(arr, k):
    print('arr: {}, k: {}'.format(arr, k))
    print('win max: {}'.format(win_max(arr, k)))

def main():
    '''生成窗口最大值数组'''
    test([4,3,5,4,3,3,6,7], 3)
    test([6,6,6,6,6,6,6,7], 3)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
