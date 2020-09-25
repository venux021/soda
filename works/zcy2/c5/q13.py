#!/usr/bin/env python3
from collections import deque
import sys

from sodacomm.tools import testwrapper

def make_palindrome(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for k in range(1, n):
        i = 0
        j = k
        while i < n and j < n:
            if s[i] == s[j]:
                if j - i >= 2:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
            i += 1
            j += 1
    min_count = dp[0][n-1]
    print(min_count)
    i, j = 0, n-1
    Lq = deque()
    Rq = deque()
    while i < j:
        if s[i] == s[j]:
            Lq.append(s[i])
            Rq.appendleft(s[j])
            i += 1
            j -= 1
        elif dp[i][j] == dp[i][j-1] + 1:
            Lq.append(s[j])
            Rq.appendleft(s[j])
            j -= 1
        else:
            Lq.append(s[i])
            Rq.appendleft(s[i])
            i += 1
    if i == j:
        Lq.append(s[i])
    buf = Lq + Rq
    return ''.join(buf)

def make_palindrome_2(s, sp):
    i, j = 0, len(sp)-1
    a, b = 0, len(s)-1
    Lq = deque()
    Rq = deque()
    while i <= j:
        c = sp[i]
        ax = a
        while s[ax] != c:
            ax += 1
        bx = b
        while s[bx] != c:
            bx -= 1
        left = s[a:ax]
        right = s[bx+1:b+1]
        Lq.append(left + ''.join(reversed(right)))
        Rq.appendleft(right + ''.join(reversed(left)))
        Lq.append(c)
        if i < j:
            Rq.appendleft(c)
        i += 1
        j -= 1
        a = ax + 1
        b = bx - 1
    return ''.join(Lq + Rq)

@testwrapper
def test(s):
    print(s)
    print(make_palindrome(s))

@testwrapper
def test2(s, sp):
    print(s, sp)
    print(make_palindrome_2(s, sp))

def main():
    test('AB')
    test('aba')
    test('A1B21C')
    test('A1BC22DE1F')
    test2('A1BC22DE1F', '1221')
    test2('A1BC2DE1F', '121')

if __name__ == '__main__':
    main()
