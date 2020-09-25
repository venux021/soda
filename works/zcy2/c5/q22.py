#!/usr/bin/env python3
import itertools
import sys

from sodacomm.tools import testwrapper

def is_match(s, e):
    return do_match(s, 0, e, 0)

def do_match(s, i, e, j):
    if j == len(e):
        return i == len(s)

    if j == len(e) - 1 or e[j+1] != '*':
        return (i < len(s) and e[j] == s[i] or e[j] == '.') and do_match(s, i+1, e, j+1)

    k = i
    while k < len(s) and (s[k] == e[j] or e[j] == '.'):
        if do_match(s, k, e, j+2):
            return True
        k += 1

    return do_match(s, k, e, j+2)

def is_match_2(s, e):
    sn = len(s)
    en = len(e)
    dp = [[False] * (en+1) for _ in range(sn+1)]
    dp[sn][en] = True
    
    for i in range(en-1, -1, -2):
        if i > 0 and e[i] == '*':
            dp[sn][i-1] = True

    if sn > 0 and en > 0:
        if s[-1] == e[-1] or e[-1] == '.':
            dp[sn-1][en-1] = True

    for j, i in itertools.product(range(en-2, -1, -1), range(sn-1, -1, -1)):
        if e[j+1] != '*':
            if e[j] == s[i] or e[j] == '.':
                dp[i][j] = dp[i+1][j+1]
        else:
            k = i
            while k < sn and (s[k] == e[j] or e[j] == '.'):
                if dp[k][j+2]:
                    dp[i][j] = True
                    break
                k += 1
            dp[i][j] = dp[i][j] or dp[k][j+2]

    return dp[0][0]

@testwrapper
def test(s, e):
    print(s, e)
    r1 = is_match(s, e)
    r2 = is_match_2(s, e)
    if r1 == r2:
        print(r1)
    else:
        print(f'ERROR: {r1} {r2}')

def main():
    test('abc', 'abc')
    test('abc', 'a.c')
    test('abcd', '.*')
    test('abcd', 'a.*d')
    test('abcd', 'a.*')
    test('abcd', 'abcd.*')
    test('abcd', '.*abcd')
    test('abcd', '.*bcd')
    test('abcd', 'a..d')
    test('abcd', 'a.de')
    test('', '.*')
    test('', '..*')

if __name__ == '__main__':
    main()
