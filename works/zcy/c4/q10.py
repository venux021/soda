#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def is_aim(s1, s2, aim):
    n1 = len(s1)
    n2 = len(s2)
    dp = [[False] * (n2+1) for i in range(n1+1)]
    dp[0][0] = True
    
    for i in range(n1):
        if s1[i] == aim[i]:
            dp[i+1][0] = True
        else:
            break

    for i in range(n2):
        if s2[i] == aim[i]:
            dp[0][i+1] = True
        else:
            break

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            dp[i][j] = (dp[i-1][j] and aim[i+j-1] == s1[i-1]
                    or dp[i][j-1] and aim[i+j-1] == s2[j-1])

    return dp[n1][n2]

def is_aim2(s1, s2, aim):
    n1 = len(s1)
    n2 = len(s2)
    dp = [[False] * (n2+1) for i in range(n1+1)]
    dp[0][0] = True

    for i in range(0, n1 + 1):
        for j in range(0, n2 + 1):
            if not dp[i][j]:
                continue
            if j < n2:
                dp[i][j+1] = dp[i][j+1] or (aim[i+j] == s2[j])
            if i < n1:
                dp[i+1][j] = (aim[i+j] == s1[i])

    return dp[n1][n2]

def dump_dp(dp):
    for i in range(len(dp)):
        line = []
        for j in range(len(dp[0])):
            line.append('1' if dp[i][j] else '0')
        print ' '.join(line)

def test(s1, s2, aim):
    print 's1: {}, s2: {}, aim: {}'.format(s1, s2, aim)
    print 'result: {}'.format(is_aim(s1, s2, aim))
    print 'result 2: {}'.format(is_aim2(s1, s2, aim))
    print '------'

def main():
    '''字符串的交错组成'''
    test('12', 'AB', 'A12B')
    test('abcde', 'ackmj', 'acbckdemj')
    test('abcde', 'ackmj', 'acabckdemj')
    test('12', '13', '1213')
    test('13', '12', '1213')
    test('aaaaaaaab', 'aaaad', 'aaaaaaaabaaaad')
    test('aab', 'aaaad', 'aaaadaab')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
