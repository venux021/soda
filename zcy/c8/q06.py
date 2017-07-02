#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random

def gen_arr(n, yes):
    if yes:
        k = n / 2 + 1
        a = [random.randint(1,100)] * k
        b = [random.randint(1,100) for i in range(n-k)]
        c = a + b
        random.shuffle(c)
        return c
    else:
        a = list(range(n))
        random.shuffle(a)
        return a

def find_more_than_half(arr):
    n = len(arr)
    low = 0
    high = n - 1
    mid = (low + high) / 2
    while True:
        p = partition(arr, low, high)
        if p > mid:
            high = p - 1
        elif p < mid:
            low = p + 1
        else:
            break
    h = arr[mid]
    times = 0
    for v in arr:
        if v == h:
            times += 1
    if times > n/2:
        return h
    else:
        return None

def partition(arr, i, j):
    pivot = arr[i]
    t = arr[i]
    while i < j:
        while i < j and arr[j] >= t:
            j -= 1
        if i < j:
            arr[i] = arr[j]
            i += 1
        while i < j and arr[i] < t:
            i += 1
        if i < j:
            arr[j] = arr[i]
            j -= 1
    arr[i] = t
    return i

def find_more_than_half2(arr):
    times = 0
    t = None
    n = len(arr)
    for v in arr:
        if times == 0:
            t = v
            times += 1
        elif v == t:
            times += 1
        else:
            times -= 1
    times = 0
    for v in arr:
        if v == t:
            times += 1

    if times > n/2:
        return t
    else:
        return None

def test(arr):
    print 'arr: {}'.format(arr)
    print 'more than half: {}'.format(find_more_than_half(arr))
    print 'more than half 2: {}'.format(find_more_than_half2(arr))

def gen_arr_k(n, k, m, yes):
    if yes:
        t = n / k
        arr = list(range(100))
        random.shuffle(arr)
        r = []
        for v in arr[:m]:
            r += ([v] * (t+1))
        r += arr[len(r)-n:]
        random.shuffle(r)
        return r
    else:
        a = list(range(n))
        random.shuffle(a)
        return a

def testk(arr, k):
    print 'arr: {}, k: {}'.format(arr, k)
    print 'more than n/k: {}'.format(find_more_than_nk(arr, k))

def find_more_than_nk(arr, k):
    m = {}
    for v in arr:
        if v not in m:
            if len(m) < k - 1:
                m[v] = 1
            else:
                for i, t in m.items():
                    if t > 1:
                        m[i] = t - 1
                    else:
                        del m[i]
        else:
            m[v] += 1

    for i in m:
        m[i] = 0

    for v in arr:
        if v in m:
            m[v] += 1

    n = len(arr)
    return map(lambda x: x[0], filter(lambda x: x[1] > n/k, m.items()))

def main():
    '''在数组中找到出现次数大于N/K的数'''
    test(gen_arr(3, True))
    test(gen_arr(10, True))
    test(gen_arr(10, False))
    testk(gen_arr_k(10, 4, 3, True), 4)
    testk(gen_arr_k(10, 4, 3, False), 4)
    testk(gen_arr_k(10, 6, 4, True), 6)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
