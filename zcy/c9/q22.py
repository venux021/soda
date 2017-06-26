#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def candy(arr):
    n = len(arr)
    c = [0] * n

    i = 0
    while i < n and c[-1] == 0:
        mid, j = slopes(arr, i)
        if i == mid and mid == j and c[i] > 0:
            i += 1
            continue
        up = mid - i + 1
        down = j - mid + 1
        top = max(up, down)
        c[mid] = top

        k = 1
        for p in range(i, mid):
            c[p] = k
            k += 1

        k = 1
        for p in range(j, mid, -1):
            c[p] = k
            k += 1

        if j > mid:
            i = j
        else:
            i = j + 1

    return c

def slopes(arr, i):
    n = len(arr)
    mid = i
    while mid + 1 < n and arr[mid + 1] > arr[mid]:
        mid += 1
    j = mid
    while j + 1 < n and arr[j+1] < arr[j]:
        j += 1
    return (mid, j)

def candy_2(arr):
    n = len(arr)
    c = [0] * n

    i = 0
    while i < n and c[-1] == 0:
        mid, j = slopes_2(arr, i)
        if i == mid and mid == j and c[i] > 0:
            i += 1
            continue
        up = arr[mid] - arr[i] + 1
        down = arr[mid] - arr[j] + 1
        top = max(up, down)
        c[mid] = top

        if c[i] == 0:
            c[i] = 1
        for p in range(i, mid):
            if arr[p] != arr[mid]:
                c[p] = c[i] + arr[p] - arr[i]
            else:
                c[p] = c[mid]

        if c[j] == 0:
            c[j] = 1
        for p in range(j, mid, -1):
            if arr[p] != arr[mid]:
                c[p] = c[j] + arr[p] - arr[j]
            else:
                c[p] = c[mid]

        if j > mid:
            i = j
        else:
            i = j + 1

    return c

def slopes_2(arr, i):
    n = len(arr)
    mid = i
    while mid + 1 < n and arr[mid+1] >= arr[mid]:
        mid += 1
    j = mid
    while j + 1 < n and arr[j+1] <= arr[j]:
        j += 1
    return (mid, j)

def test(arr):
    print 'arr: {}'.format(arr)
    a1 = candy(arr)
    print 'candy: {}, sum: {}'.format(a1, sum(a1))
    a2 = candy_2(arr)
    print 'candy 2: {}, sum: {}'.format(a2, sum(a2))

def main():
    '''分糖果问题'''
    test([1,2,2])
    test([1,2,2,1])
    test([1,2,3,2,1])
    test([1,4,5,9,3,2])
    test([3,2,2,3,4])
    test([3,5,5,3,1])
    test([0,1,2,3,3,3,2,2,2,2,2,1,1])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
