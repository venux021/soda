#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def get_max_size(mx):
    n = len(mx)    # row count
    m = len(mx[0]) # col count
    height = [0] * m
    max_size = 0
    for i in range(n):
        for j in range(m):
            if mx[i][j] == 1:
                height[j] += 1
            else:
                height[j] = 0
        max_size = max(max_size, calculate(height))
    return max_size

def calculate(height):
    height = height + [0]
    stk = []
    max_size = 0
    for i in range(len(height)):
        while stk and height[stk[-1]] > height[i]:
            j = stk.pop()
            R = i - j
            if stk:
                L = j - stk[-1]
            else:
                L = j + 1
            size = height[j] * (L + R - 1)
            max_size = max(max_size, size)
        stk.append(i)
    return max_size

@testwrapper
def test(mx):
    msize = get_max_size(mx)
    print(mx)
    print(msize)

def main():
    test([[1,1,1,0]])
    test([[1,0,1,1],[1,1,1,1],[1,1,1,0]])

if __name__ == '__main__':
    main()
