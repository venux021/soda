#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def min_cut(s):
    n = len(s)
    dp = [sys.maxsize] * n
    dp[0] = 0
    p = [[False] * n for _ in range(n)]
    for i in range(n):
        p[i][i] = True

    def is_palindrome(x, y):
        if x > y:
            x, y = y, x
        if x == y:
            return True
        elif x + 1 == y:
            return s[x] == s[y]
        else:
            return s[x] == s[y] and p[x+1][y-1]

    for i in range(1, n):
        for j in range(i, -1, -1):
            if is_palindrome(j, i):
                p[j][i] = True
                if j > 0:
                    dp[i] = min(dp[i], dp[j-1] + 1)
                else:
                    dp[i] = 0

    return dp[-1]

@testwrapper
def test(s):
    print(s)
    print(min_cut(s))

def main():
    test('ABA')
    test('ACDCDCDAD')
    test('abcdefg')
    test('abaaca')

if __name__ == '__main__':
    main()
