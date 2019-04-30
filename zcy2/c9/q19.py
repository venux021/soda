#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def find_num_from_rotate(arr, num):
    n = len(arr)
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == num:
            return mid
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            while arr[low] == arr[mid] and low <= mid:
                low += 1
        elif arr[low] != arr[mid]:
            if arr[mid] > arr[low]:
                if num >= arr[low] and num < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if num > arr[mid] and num <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        else:
            if arr[mid] < arr[high]:
                if num > arr[mid] and num <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if num < arr[mid] and num >= arr[low]:
                    high = mid - 1
                else:
                    low = mid + 1
    return -1

@testwrapper
def test(arr, num):
    print(arr, num)
    print(find_num_from_rotate(arr, num))

def main():
    test([1,2,3,4,5], 3)
    test([1,2,3,4,5], 1)
    test([1,2,3,4,5], 5)
    test([1,2,3,4,5], 0)
    test([1,2,3,4,5], 6)
    test([3,4,5,1,2], 5)
    test([3,4,5,1,2], 1)
    test([3,4,5,1,2], 3)
    test([3,4,5,1,2], 2)
    test([3,4,5,1,2], 4)
    test([2,2,2,2,2,3,4,5,1,2,2], 5)
    test([2,2,2,2,2,2,2,2,2,3,4,5,1,2,2], 1)

if __name__ == '__main__':
    main()
