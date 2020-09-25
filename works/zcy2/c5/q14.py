#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def is_valid_parenthesis(s):
    stk = []
    for c in s:
        if c == '(':
            stk.append(c)
        elif c == ')':
            if not stk:
                return False
            stk.pop()
        else:
            return False
    return bool(not stk)

def longest_parenthesis(s):
    n = len(s)
    dp = [0] * n
    max_len = 0
    for i in range(1, n):
        if s[i] == ')':
            if s[i-1] == '(':
                if i >= 2:
                    dp[i] = dp[i-2] + 2
                else:
                    dp[i] = 2
            elif s[i-1] == ')':
                j = i - dp[i-1] - 1
                if j >= 0 and s[j] == '(':
                    dp[i] = dp[i-1] + 2
                else:
                    dp[i] = 0
        else:
            dp[i] = 0
        max_len = max(max_len, dp[i])
    return max_len

@testwrapper
def test(s):
    print(s)
    print(is_valid_parenthesis(s))
    print(longest_parenthesis(s))

def main():
    test('()')
    test('(()())')
    test('(())')
    test('())')
    test('()(')
    test('()a()')
    test('()(()()(')

if __name__ == '__main__':
    main()
