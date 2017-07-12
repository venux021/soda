#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def merge_s(arr, start, end, tmp):
    if start == end:
        return 0

    mid = (start + end) // 2 + 1

    left_count = merge_s(arr, start, mid-1, tmp)
    right_count = merge_s(arr, mid, end, tmp)
    total = left_count + right_count

    L = mid-1
    R = end
    i = end

    while R >= mid and L >= start:
        if arr[L] > arr[R]:
            total += (R - mid + 1)
            tmp[i] = arr[L]
            L -= 1
        else:
            tmp[i] = arr[R]
            R -= 1
        i -= 1

    while R >= mid:
        tmp[i] = arr[R]
        R -= 1
        i -= 1

    for j in range(L+1, end+1):
        arr[j] = tmp[j]

    return total

def get_peers(arr):
    n = len(arr)
    tmp = [0] * n

    return merge_s(arr, 0, n-1, tmp)

def test(arr):
    print('arr: {}'.format(arr))
    print('peers: {}'.format(get_peers(arr)))

def main():
    '''数组中的逆序对'''
    test([7,5,6,4])
    test([7,5,6,4,1])
    test([7,5,6,4,1,3])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
