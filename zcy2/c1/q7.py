#!/usr/bin/env python3
from collections import deque
import sys

def max_win(arr, w):
    q = deque()
    r = []
    for i, v in enumerate(arr):
        while q and arr[q[-1]] < v:
            q.pop()
        q.append(i)
        if i - q[0] >= w:
            q.popleft()
        if i >= w-1:
            r.append(arr[q[0]])

    return r

def test(arr, w):
    print(arr, w)
    print(max_win(arr, w))
    print('--------')

def main():
    '''生成窗口最大值数组'''
    test([4,3,5,4,3,3,6,7], 3)

if __name__ == '__main__':
    main()
