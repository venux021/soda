#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def min_jump(arr):
    n = len(arr)
    far = next_far = arr[0]
    if far >= n-1:
        return 1
    jump = 1
    for i in range(1, n):
        next_far = max(arr[i] + i, next_far)
        if next_far >= n-1:
            jump += 1
            break
        if i == far:
            far = next_far
            jump += 1
    return jump

def test(arr):
    print 'arr: {}'.format(arr)
    print 'min jump: {}'.format(min_jump(arr))

def main():
    '''跳跃游戏'''
    test([3,2,3,1,1,4])
    test([7,1,2,3,5,1,1,1,1,1])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
