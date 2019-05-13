#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def manacher(s):
    n = len(s)
    N = n*2+1
    buf = [None] * N
    for i, c in enumerate(s):
        buf[i*2] = '#'
        buf[i*2+1] = s[i]
    buf[-1] = '#'

    radius = [0] * N
    radius[0] = 1
    index = 0
    rbound = 0
    e_len = 0
    e_index = -1
    for i in range(1,N):
        if i > rbound:
            R = dofind(buf, i)
            index = i
            radius[i] = R
            rbound = i + R - 1
        else:
            _i = index * 2 - i
            _r = radius[_i]
            if i + _r - 1 < rbound:
                radius[i] = _r
            elif i + _r - 1 > rbound:
                radius[i] = rbound - i + 1
            else:
                radius[i] = dofind(buf, i, rbound - i + 1)

    return max(radius) - 1

def make_palindrome(s):
    n = len(s)
    N = n*2+1
    buf = [None] * N
    for i, c in enumerate(s):
        buf[i*2] = '#'
        buf[i*2+1] = s[i]
    buf[-1] = '#'

    radius = [0] * N
    radius[0] = 1
    index = 0
    rbound = 0
    k = -1
    for i in range(1,N):
        if i > rbound:
            R = dofind(buf, i)
            index = i
            radius[i] = R
            rbound = i + R - 1
            if rbound == N - 1:
                k = radius[i] - 1
                break
        else:
            _i = index * 2 - i
            _r = radius[_i]
            if i + _r - 1 < rbound:
                radius[i] = _r
            elif i + _r - 1 > rbound:
                radius[i] = rbound - i + 1
            else:
                radius[i] = dofind(buf, i, rbound - i + 1)
                rb = i + radius[i] - 1
                if rbound < rb:
                    rbound = rb
                    if rbound == N-1:
                        k = radius[i] - 1
                        break

    return ''.join(reversed(s[:n-k]))

def dofind(arr, i, r = 1):
    n = len(arr)
    while i-r >= 0 and i+r < n and arr[i-r] == arr[i+r]:
        r += 1
    return r

@testwrapper
def test(s):
    print(s)
    print(manacher(s))
    print(make_palindrome(s))

def main():
    test('123')
    test('abc1234321ab')
    test('abacaba')
    test('1221')
    test('CabaddabaC')
    test('abacabd')
    test('dabacabac')

if __name__ == '__main__':
    main()
