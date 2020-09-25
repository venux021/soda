#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def do_match(s, e):
    return is_match(s, 0, e, 0)

def is_match(s, i, e, j):
    if j == len(e):
        return i == len(s)
    elif j + 1 == len(e) or e[j+1] != '*':
        return i < len(s) and (s[i] == e[j] or e[j] == '.') and is_match(s, i+1, e, j+1)
    while i < len(s) and (s[i] == e[j] or e[j] == '.'):
        if is_match(s, i, e, j+2):
            return True
        i += 1
    return is_match(s, i, e, j+2)

def do_match2(s, p):
    sn = len(s)
    pn = len(p)
    dp = [[False] * (pn+1) for i in range(sn+1)]

    dp[sn][pn] = True

    for i in range(pn-1, 0, -2):
        if p[i] == '*':
            dp[sn][i-1] = True
        else:
            break

    if pn > 0 and p[-1] != '*':
        for i in range(sn):
            dp[i][pn-1] = (p[-1] == s[i] or p[-1] == '.') and dp[i+1][pn]

    for j in range(pn-2, -1, -1):
        for i in range(sn-1, -1, -1):
            if p[j+1] != '*':
                dp[i][j] = (s[i] == p[j] or p[j] == '.') and dp[i+1][j+1]
            else: # p[j+1] == '*'
                k = i
                while k < sn and (s[k] == p[j] or p[j] == '.'):
                    if dp[k][j+2]:
                        dp[i][j] = True
                        break
                    k += 1
                if not dp[i][j]:
                    dp[i][j] = dp[k][j+2]

    return dp[0][0]

@testwrapper
def test(s, e):
    print(f'string: {s}')
    print(f'pattern: {e}')
    a = do_match(s,e)
    b = do_match2(s, e)
    if a == b:
        print(a)
    else:
        raise Exception('error')

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
    test('', 'a*b*.*c*')
    test('', 'ba*b*.*c*')
    test('aa', 'a')
    test('aa', 'a*')
    test('ab', '.*')
    test('aab', 'c*a*b')
    test('mississippi', 'mis*is*p*.')
    test('a', '')
    test('mississippi', 'mis*is*ip*.')

if __name__ == '__main__':
    main()
