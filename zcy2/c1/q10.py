#!/usr/bin/env python3
from collections import deque
import sys

from sodacomm.tools import testwrapper

def get_num(arr, num):
    n = len(arr)
    if n == 0:
        return 0
    qmax = deque([0])
    qmin = deque([0])
    i = 0
    j = 1
    total = 0
    def _update_max(k):
        while qmax and arr[qmax[-1]] < arr[k]:
            qmax.pop()
        qmax.append(k)
    def _update_min(k):
        while qmin and arr[qmin[-1]] > arr[k]:
            qmin.pop()
        qmin.append(k)
    while i < n:
        _max = qmax[0]
        _min = qmin[0]
        if _max - _min <= num and j < n:
            _update_max(j)
            _update_min(j)
            j += 1
        else:
            total += (j - i)
            i += 1
            if qmax[0] < i:
                qmax.popleft()
            if qmin[0] < i:
                qmin.popleft()
    return total

@testwrapper
def test(arr, num):
    print(f'{arr} {num}')
    print(get_num(arr, num))

def main():
    test([3,1,6,2,9,4,5], 3)

if __name__ == '__main__':
    main()
