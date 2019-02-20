#!/usr/bin/env python3
from collections import deque
import sys

from sodacomm.tools import testwrapper

def window_max(arr, w):
    if not arr or not w or w > len(arr):
        return []
    n = len(arr)
    wm = []
    q = deque()
    for i in range(n):
        while q and arr[q[-1]] <= arr[i]:
            q.pop()
        q.append(i)
        if i < w - 1:
            continue
        while i - q[0] >= w:
            q.popleft()
        wm.append(arr[q[0]])
    return wm

@testwrapper
def test(arr, w):
    wm = window_max(arr, w)
    print(arr)
    print(wm)

def main():
    test([4,3,5,4,3,3,6,7], 3)
    test([3,6,1,4,6,2,5,2,4], 3)
    test([3,6,1,4,6,2,5,2,4], 1)
    test([3,6,1,4,6,2,5,2,4], 9)

if __name__ == '__main__':
    main()
