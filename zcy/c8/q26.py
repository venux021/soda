#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def max_diff(arr):
    n = len(arr)
    Min = Max = arr[0]
    for i in range(1, n):
        Min = min(Min, arr[i])
        Max = max(Max, arr[i])

    size = (Max - Min) / float(n)
    buckets = [[Max, Min, 0] for i in range(n+1)]
    buckets[n] = [Max, Max, 1]

    for num in arr:
        index = int((num - Min) / size)
        buckets[index][0] = min(buckets[index][0], num)
        buckets[index][1] = max(buckets[index][1], num)
        buckets[index][2] += 1

    i = 0
    mdiff = 0
    while i < n:
        j = i + 1
        while buckets[j][2] == 0:
            j += 1
        if j - 1 > i:
            mdiff = max(mdiff, buckets[j][0] - buckets[i][1])
        i = j

    return mdiff

def test(arr):
    print 'arr: {}'.format(arr)
    print 'max diff: {}'.format(max_diff(arr))

def main():
    '''数组排序之后相邻数的最大差值'''
    test([9,3,1,10])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
