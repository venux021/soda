#!/usr/bin/env python3
import itertools
import sys

from sodacomm.tools import testwrapper

def drop_chess(N, K):
    dp = [[0] * (K+1) for i in range(N+1)]
    for i in range(1, N+1):
        dp[i][1] = i

    for k, n in itertools.product(range(2, K+1), range(1,N+1)):
        _min = sys.maxsize
        for i in range(1, n+1):
            _min = min(_min, max(dp[i-1][k-1], dp[n-i][k]))
        dp[n][k] = _min + 1

    return dp[N][K]

def drop_chess_2(N, K):
    dp = [[0] * (K+1) for i in range(N+1)]
    first = [[0] * (K+1) for i in range(N+1)]
    for i in range(1, N+1):
        dp[i][1] = i
        first[i][1] = 1

    for n, k in itertools.product(range(1,N+1), range(K,1,-1)):
        _min = sys.maxsize
        i_min = -1
        upper = first[n][k+1] if k < K else n
        lower = max(1, first[n-1][k])
        for i in range(lower, upper+1):
            _mx = max(dp[i-1][k-1], dp[n-i][k])
            if _mx < _min:
                _min = _mx
                i_min = i
        dp[n][k] = _min + 1
        first[n][k] = i_min

    return dp[N][K]

def drop_chess_3(N, K):
    max_times = log2(N)
    if K >= max_times:
        return max_times
    arr = [[0] * (K+1) for i in range(2)] 
    for i in range(1,K+1):
        arr[0][i] = 1
    T = 2
    p = 1
    while True:
        q = 1 - p
        for i in range(1, K+1):
            arr[p][i] = arr[q][i] + arr[q][i-1] + 1
            if arr[p][i] >= N:
                return T
        T += 1
        p = 1 - p

def log2(n):
    i = 0
    while n >= 2:
        i += 1
        n >>= 1
    return i

@testwrapper
def test(N, K):
    print(N, K)
    print(drop_chess(N, K))
    print(drop_chess_2(N, K))
    print(drop_chess_3(N, K))

def main():
    test(10, 1)
    test(3, 2)
    test(105, 2)
    test(200, 3)
    test(1000, 6)
    test(1000, 5)

if __name__ == '__main__':
    main()
