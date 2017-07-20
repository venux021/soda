#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import math

def rebuild(arr):
    arr = arr[:]
    arr.sort()
    n = len(arr)
    k = int((math.sqrt(8*n+1)+1)/2)
    loc = [0] * k
    loc[-1] = arr[-1]
    arr.pop()

    dist = {}
    for v in arr:
        dist[v] = dist.get(v, 0) + 1
    if rbd(dist, k - 2, loc, 1, k-2):
        return loc

def find_max(dist):
    m = 0
    for k, v in dist.items():
        if v > 0 and k > m:
            m = k
    return m

def rbd(dist, num_p, loc, left, right):
    if num_p == 0:
        return True

    max_d = find_max(dist)

    seq = [j for j in range(0, left)] + [j for j in range(right+1, len(loc))]

    R = max_d
    loc[right] = R
    to_remove = []
    for i in seq:
        d = abs(R - loc[i])
        if dist[d] > 0:
            to_remove.append(d)
        else:
            break
    else:
        to_remove.append(max_d)
        for t in to_remove:
            dist[t] -= 1
        if rbd(dist, num_p - 1, loc, left, right - 1):
            return True
        for t in to_remove:
            dist[t] += 1

    L = loc[-1] - max_d
    loc[left] = L
    to_remove = []
    for i in seq:
        d = abs(L - loc[i])
        if dist[d] > 0:
            to_remove.append(d)
        else:
            break
    else:
        to_remove.append(max_d)
        for t in to_remove:
            dist[t] -= 1
        if rbd(dist, num_p - 1, loc, left+1, right):
            return True
        for t in to_remove:
            dist[t] += 1

    return False

def test(arr):
    print('arr:', arr)
    print('loc:', rebuild(arr))

def main():
    '''收费公路重建问题'''
    test([1,2,2,2,3,3,3,4,5,5,5,6,7,8,10])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
