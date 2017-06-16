#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def part(arr):
    i = -1
    j = 0
    v = arr[j]
    while True:
        i += 1
        if i < j:
            arr[j] = arr[i]
            arr[i] = v
        while j < len(arr) and arr[j] <= v:
            j += 1
        if j < len(arr):
            v = arr[j]
        else:
            break
    return arr

def test(arr):
    print 'arr: {}'.format(arr)
    print 'part: {}'.format(part(arr))

def main():
    '''数组的partition调整'''
    test([1,2,2,2,3,3,4,5,6,6,7,7,8,8,8,9])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
