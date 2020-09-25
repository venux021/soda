#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from collections import deque

def num_sub_arr(arr, k):
    n = len(arr)
    qmax = deque()
    qmin = deque()
    count = 0
    i = j = 0
    while j < n:

        while qmax and arr[qmax[-1]] <= arr[j]:
            qmax.pop()
        qmax.append(j)

        while qmin and arr[qmin[-1]] >= arr[j]:
            qmin.pop()
        qmin.append(j)

        while i <= j and arr[qmax[0]] - arr[qmin[0]] > k:
            count += (j - i)
            if qmax[0] == i:
                qmax.popleft()
            if qmin[0] == i:
                qmin.popleft()
            i += 1

        j += 1

    count += int((j-i)*(j-i+1)/2)
    return count

def test(arr, k):
    print('arr: {}, k: {}'.format(arr, k))
    print('count of sub array: {}'.format(num_sub_arr(arr, k)))
    print('------')

def main():
    '''最大值减去最小值小于或等于num的子数组数量'''
    test([1,2,3], 2)
    test([1,1,1], -1)
    test([3,7,4,1,2,5,8,6,0], 5)
    test([3,7,4,1,2,5,8,6,0], 1)
    test([3,7,4,1,2,5,8,6,0], 10)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
