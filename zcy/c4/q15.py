#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def jump(arr):
    n = len(arr)
    if n == 0:
        return -1
    elif n == 1:
        return 0
    J = 0
    limit = 0
    farest = arr[0]
    for i in range(1,n):
        if i > limit:
            J += 1
            limit = farest
            if limit < i:
                return -1
            elif limit >= n-1:
                return J
        farest = max(farest, arr[i] + i)

def test(arr):
    print 'arr: {}'.format(arr)
    print 'jump: {}'.format(jump(arr))

def main():
    '''跳跃游戏'''
    test([3,2,3,1,1,4])
    test([3,2,3,2,1,0,2])
    test([5,1])
    test([0,2])
    test([0])
    test([1])
    test([10])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
