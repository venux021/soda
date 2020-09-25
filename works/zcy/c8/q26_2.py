#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

class Bucket(object):

    def __init__(self):
        self.min = 0x7fffffff
        self.max = -0x7fffffff
        self.count = 0

    def add(self, num):
        self.min = min(self.min, num)
        self.max = max(self.max, num)
        self.count += 1

def max_diff(arr):
    n = len(arr)
    _min = min(arr)
    _max = max(arr)

    step = (_max - _min) / n
    if step == 0:
        step += 1

    buckets = [Bucket() for i in range(n+1)]

    for a in arr:
        if a == _max:
            buckets[n].add(a)
        else:
            k = (a - _min) / step
            buckets[k].add(a)

    if buckets[0].count == 0:
        return 0
    i = 0
    mxdf = 0
    while i < n:
        j = i + 1
        while buckets[j].count == 0:
            j += 1
        mxdf = max(mxdf, buckets[j].min - buckets[i].max)
        i = j

    return mxdf

def test(arr):
    print 'arr: {}'.format(arr)
    print 'max diff: {}'.format(max_diff(arr))

def main():
    '''数组排序之后相邻数的最大差值'''
    test([9,3,1,10])
    test([5,5,5,5])
    test([76,43,55,23,45,10,112,111,19,68])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
