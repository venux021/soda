#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def post_office_dist(arr, num):
    R = num
    C = len(arr)
    dp = [[0] * C for i in range(R+1)]
    w = [[0] * C for i in range(C)]

    for i in range(C):
        for j in range(i+1,C):
            w[i][j] = w[j][i] = w[i][j-1] + arr[j] - arr[(i+j)//2]

    for i in range(C):
        dp[1][i] = w[0][i]

    for i in range(2,R+1):
        for j in range(i+1,C):
            _min = sys.maxsize
            for k in range(i-2, j):
                v = dp[i-1][k] + w[k+1][j]
                _min = min(_min, v)
            dp[i][j] = _min

    return dp[num][C-1]

@testwrapper
def test(arr, num):
    print(arr, num)
    print(post_office_dist(arr, num))

def main():
    test([1,2,3,4,5,1000], 2)
    test([-3,-2,-1,0,1,2], 3)

if __name__ == '__main__':
    main()
