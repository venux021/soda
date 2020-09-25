#!/usr/bin/env python3
import itertools
import sys

from sodacomm.tools import testwrapper

def is_interlaced(seq, s1, s2):
    if not seq:
        return True
    R = len(s1) + 1
    C = len(s2) + 1
    dp = [[0] * C for _ in range(R)]
    k = 0
    for i in range(1,C):
        if seq[i-1] == s2[i-1]:
            k += 1
        dp[0][i] = k
    k = 0
    for j in range(1,R):
        if seq[j-1] == s1[j-1]:
            k += 1
        dp[j][0] = k
    for i, j in itertools.product(range(1,R), range(1,C)):
        if s1[i-1] == seq[dp[i-1][j]]:
            dp[i][j] = dp[i-1][j] + 1
        if s2[j-1] == seq[dp[i][j-1]]:
            dp[i][j] = max(dp[i][j], dp[i][j-1] + 1)
        if dp[i][j] == len(seq):
            return True
    return False

@testwrapper
def test(seq, s1, s2):
    print(seq, s1, s2)
    print(is_interlaced(seq, s1, s2))

def main():
    test('AB12', 'AB', '12')
    test('B1A2', 'AB', '12')
    test('A1B2', 'AB', '12')
    test('A12B', 'AB', '12')
    test('1A2B', 'AB', '12')
    test('1AB2', 'AB', '12')

if __name__ == '__main__':
    main()
