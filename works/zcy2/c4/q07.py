#!/usr/bin/env python3
import itertools
import sys

from sodacomm.tools import testwrapper

def longest_common_seq(a1, a2):
    m = len(a1)
    n = len(a2)
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        if a1[i] == a2[0]:
            dp[i][0] = 1
    for i in range(n):
        if a2[i] == a1[0]:
            dp[0][i] = 1
    for i, j in itertools.product(range(1,m), range(1,n)):
        if a1[i] == a2[j]:
            dp[i][j] = max(dp[i-1][j-1] + 1, dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    buf = []
    i, j = m-1, n-1
    while i >= 0 and j >= 0:
        if a1[i] == a2[j]:
            buf.append(a1[i])
            i-=1
            j-=1
        elif dp[i][j] == dp[i-1][j]:
            i-=1
        else:
            j-=1

    return list(reversed(buf))

@testwrapper
def test(a1, a2):
    print(a1, a2)
    print(longest_common_seq(a1, a2))

def main():
    test('1A2C3D4B56', 'B1D23CA45B6A')

if __name__ == '__main__':
    main()
