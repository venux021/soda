#!/usr/bin/env python3
import re
import sys

from sodacomm.tools import testwrapper

def convert(s):
    s = re.sub('10', 'a', s)
    return re.sub('20', 'b', s)

def string_count(s):
    s = convert(s)
    if not s or '0' in s:
        return 0
    n = len(s)
    dp = [0] * len(s)
    dp[0] = 1
    for i in range(1, n):
        if s[i-1] in '3456789ab' or s[i-1] == '1' and s[i] in 'ab' or s[i-1] == '2' and s[i] in '789ab':
            dp[i] = dp[i-1]
        else:
            if i < 2:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]

@testwrapper
def test(s):
    print(s)
    print(string_count(s))

def main():
    test('1111')
    test('01')
    test('10')
    test('1203231')
    test('121213')

if __name__ == '__main__':
    main()
