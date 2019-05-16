#!/usr/bin/env python3
import itertools
import sys

from sodacomm.tools import testwrapper

def painter(pictures, N):
    np = len(pictures)
    dp = [[0] * np for i in range(N+1)]
    cost = [[0] * np for i in range(np)]

    for i in range(1, N+1):
        dp[i][0] = pictures[0]

    c = 0
    for i in range(np):
        c += pictures[i]
        dp[1][i] = c

    for i in range(np):
        c = 0
        for j in range(i, np):
            c += pictures[j]
            cost[i][j] = c

    for i, j in itertools.product(range(2,N+1), range(1,np)):
        _min = sys.maxsize
        for k in range(1,j+1):
            v = max(cost[k][j], dp[i-1][k-1])
            _min = min(_min, v)
        dp[i][j] = _min

    return dp[N][np-1]

def painter2(pictures, N):
    np = len(pictures)
    dp = [[0] * np for i in range(N+1)]
    cost = [[0] * np for i in range(np)]

    for i in range(1, N+1):
        dp[i][0] = pictures[0]

    c = 0
    for i in range(np):
        c += pictures[i]
        dp[1][i] = c

    for i in range(np):
        c = 0
        for j in range(i, np):
            c += pictures[j]
            cost[i][j] = c


    uppers = [-1] * np
    for i in range(2,N+1):
        for j in range(1,np):
            _min = sys.maxsize
            min_i = -1
            upp = max(1, uppers[j])
            for k in range(upp, j+1):
                v = max(cost[k][j], dp[i-1][k-1])
                if v < _min:
                    _min = v
                    min_i = k
            dp[i][j] = _min
            uppers[j] = min_i

    return dp[N][np-1]

def get_need_num(pics, limit):
    res = 1
    _sum = 0
    for p in pics:
        if p > limit:
            return sys.maxsize
        _sum += p
        if _sum > limit:
            res += 1
            _sum = p
    return res

def painter3(pics, N):
    low = 0
    high = sum(pics)
    if len(pics) < N:
        return max(pics)
    while low < high - 1:
        mid = (low + high) // 2
        if get_need_num(pics, mid) > N:
            low = mid
        else:
            high = mid
    return high

@testwrapper
def test(pics, N):
    print(pics, N)
    print(painter(pics, N))
    print(painter2(pics, N))
    print(painter3(pics, N))

def main():
    test([3,1,4], 2)
    test([1,1,1,4,3], 3)

if __name__ == '__main__':
    main()
