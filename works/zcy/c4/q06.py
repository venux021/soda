#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def show_hanoi(n, F, M, T):
    if n == 1:
        print 'move from {} to {}'.format(F, T)
        return
    show_hanoi(n-1, F, T, M)
    print 'move from {} to {}'.format(F, T)
    show_hanoi(n-1, M, F, T)

def test1(n):
    show_hanoi(n, 'left', 'mid', 'right')
    print '----'

def test2(arr):
    print 'arr: {}'.format(arr)
    print 'seq 1: {}'.format(get_seq(arr))
    print 'seq 2: {}'.format(get_seq_2(arr))
    print '----'

def get_seq_2(arr):
    F, M, T = 1,2,3
    n = len(arr)
    res = 0

    for i in range(n-1, -1, -1):
        if arr[i] == M:
            return -1
        elif arr[i] == F:
            tmp = T
            T = M
        else:
            res += (1 << i)
            tmp = F
            F = M
        M = tmp
    return res

def get_seq(arr):
    return gs(arr, len(arr), 1, 2, 3)

def gs(arr, n, F, M, T):
    if n == 1:
        if arr[n-1] == M:
            return -1
        elif arr[n-1] == F:
            return 0
        else:
            return 1
    if arr[n-1] == M:
        return -1
    elif arr[n-1] == F:
        return gs(arr, n-1, F, T, M)
    else:
        k = gs(arr, n-1, M, F, T)
        if k == -1:
            return -1
        else:
            return (1 << (n-1)) + k

def main():
    '''汉诺塔问题'''
#    test1(1)
#    test1(2)
#    test1(4)
    test2([3,3,2,1])
    test2([1,1])
    test2([2,1])
    test2([3,3])
    test2([2,2])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
