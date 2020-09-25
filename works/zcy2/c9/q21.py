#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def least_candy_fair(arr):
    n = len(arr)
    if n < 2:
        return n
    i = 0
    res = 0
    while True:
        asc_len, asc_height = find_ascend_fair(arr, i)
        a1, a2 = i, i + asc_len - 1
        i = a2
        desc_len, desc_height = find_descend_fair(arr, i)
        b1, b2 = i, i + desc_len - 1
        i = b2
        
        if asc_height >= desc_height:
            res += cal_asc(arr, a1, a2, asc_height) + cal_desc(arr, b1+1, b2)
        else:
            res += cal_asc(arr, a1, a2, desc_height) + cal_desc(arr, b1+1, b2)

        if i == n-1:
            break
        else:
            res -= 1
            i += 1
    return res

def cal_asc(arr, i1, i2, max_value):
    if i1 > i2:
        return 0
    peek = arr[i2]
    num_peek = 0
    res = 1
    cur = 1
    for i in range(i1+1, i2+1):
        if arr[i] > arr[i-1]:
            cur += 1
        res += cur
        if arr[i] == peek:
            num_peek += 1

    if max_value > cur:
        res += num_peek * (max_value - cur)
    return res

def cal_desc(arr, a1, a2):
    if a1 > a2:
        return 0
    res = 1
    cur = 1
    for i in range(a2-1, a1-1, -1):
        if arr[i] > arr[i+1]:
            cur += 1
        res += cur
    return res

def find_ascend_fair(arr, i):
    begin = i
    i += 1
    height = 1
    while i < len(arr) and arr[i] >= arr[i-1]:
        if arr[i] > arr[i-1]:
            height += 1
        i += 1
    return ((i - begin), height)

def find_descend_fair(arr, i):
    begin = i
    i += 1
    height = 1
    while i < len(arr) and arr[i] <= arr[i-1]:
        if arr[i] < arr[i-1]:
            height += 1
        i += 1
    return ((i - begin), height)

def least_candy(arr):
    n = len(arr)
    if n < 2:
        return n
    i = 0
    res = 0
    while True:
        asc_size = find_ascend(arr, i)
        i = i + asc_size - 1
        desc_size = find_descend(arr, i)
        i = i + desc_size - 1

        if asc_size >= desc_size:
            res += (cal(asc_size) + cal(desc_size-1))
        else:
            res += (cal(asc_size-1) + cal(desc_size))

        if i == n-1:
            break
        elif arr[i+1] > arr[i]:
            res -= 1
        else:
            i += 1
    return res

def cal(n):
    return n * (n+1) // 2

def find_ascend(arr, i):
    j = i
    i += 1
    while i < len(arr) and arr[i] > arr[i-1]:
        i += 1
    return i - j

def find_descend(arr, i):
    j = i
    i += 1
    while i < len(arr) and arr[i] < arr[i-1]:
        i += 1
    return i - j

@testwrapper
def test1(arr):
    print(arr)
    print(least_candy(arr))

@testwrapper
def test2(arr):
    print(arr)
    print('fair:', least_candy_fair(arr))

def main():
    test1([1,2,2])
    test1([1,2,3,2,1])
    test1([1,2,2,1])
    test1([1,2,3,1,2])
    test1([1,4,5,9,3,2])
    test1([3,2,2,3])
    test2([1,2,2])
    test2([1,2,3,2,1])
    test2([0,1,2,3,3,3,2,2,2,2,2,1,1])

if __name__ == '__main__':
    main()
