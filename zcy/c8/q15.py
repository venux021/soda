#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def adjusted(arr):
    n = len(arr)
    for i in range(n):
        if i % 2 == 1 and arr[i] % 2 == 0:
            for j in range(i+1, n, 2):
                if arr[j] % 2 == 1:
                    t = arr[i]
                    arr[i] = arr[j]
                    arr[j] = t
                    break
            else:
                return arr
        if i % 2 == 0 and arr[i] % 2 == 1:
            for j in range(i+1, n, 2):
                if arr[j] % 2 == 0:
                    t = arr[i]
                    arr[i] = arr[j]
                    arr[j] = t
                    break
            else:
                return arr
    return arr

def test(arr):
    print 'arr: {}'.format(arr)
    print 'new: {}'.format(adjusted(arr))

def main():
    '''奇数位全是奇数或偶数位全是偶数'''
    test([3,7,9,2,6,2,8,1,5,8,3,6,4])
    test([10,7,4,2,6,2,8,1,6,8,3,6,4])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
