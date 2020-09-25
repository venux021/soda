#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def find_min_from_rotate(arr):
    n = len(arr)
    low = 0
    high = n-1
    while low < high-1:
        if arr[low] < arr[high]:
            break
        mid = (low + high) // 2
        if arr[mid] > arr[high]:
            low = mid
        elif arr[mid] < arr[low]:
            high = mid
        else:
            i = low
            while i < high and arr[i] == arr[low]:
                i += 1
            if i == high:
                break
            elif arr[i] < arr[low]:
                return arr[i]
            else:
                low = i
    return min(arr[low], arr[high])

@testwrapper
def test(arr):
    print(arr)
    print(find_min_from_rotate(arr))

def main():
    test([1,2,3,4,5])
    test([2,3,4,5,1])
    test([5,1,2,3,4])
    test([2,2,2,2,1,2,2,2])
    test([2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,4,5,-1,0,1,2,2,2])
    test([2,2,3,4,5,-1,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
    test([2,2,2,2,2])

if __name__ == '__main__':
    main()
