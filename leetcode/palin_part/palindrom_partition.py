#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def partition2(s):
    n = len(s)
    if n == 0:
        return []

    isp = [[0] * n for i in range(n)]
    part = [[] for i in range(n+1)]
    part[n].append([])

    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j-i<2 or isp[i+1][j-1]):
                isp[i][j] = 1
                for tk in part[j+1]:
                    tokens = [j+1]
                    tokens.extend(tk)
                    part[i].append(tokens)

    results = []
    for pt in part[0]:
        tokens = []
        i = 0
        for v in pt:
            tokens.append(s[i:v])
            i = v
        results.append(tokens)
    return results

def partition(s):
    n = len(s)
    if n == 0:
        return []

    isp = [[0] * n for i in range(n)]
    for i in range(n):
        isp[i][i] = 1
        if i < n-1 and s[i] == s[i+1]:
            isp[i][i+1] = 1

    for L in range(3, n+1):
        for i in range(n-L+1):
            j = i + L - 1
            if s[i] == s[j]:
                isp[i][j] = isp[i+1][j-1]

    part = [[] for i in range(n)]
    part[n-1].append([n])

    for i in range(n-2, -1, -1):
        for j in range(i, n-1):
            if isp[i][j]:
                for tk in part[j+1]:
                    tokens = [j+1]
                    tokens.extend(tk)
                    part[i].append(tokens)

        if isp[i][n-1]:
            part[i].append([n])

    results = []
    for pt in part[0]:
        tokens = []
        i = 0
        for v in pt:
            tokens.append(s[i:v])
            i = v
        results.append(tokens)
    return results

@testwrapper
def test(s):
    print(s)
    print(partition2(s))

def main():
    test('aab')
    test('abbacab')
    test('aba')
    test('aabaca')
    test('a')
#    test('fddsdfasdfsddsadsdfadsdfasdfasdfaasdfafsdfsdadfasdfasdfasdfaddfdasdf')
#    test('vdsfsacxvsadfazzdfsdvzsddzcvddasdfdcvxfadxcvzdfsdzxvcxdfdx')

if __name__ == '__main__':
    main()
