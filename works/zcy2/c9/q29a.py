#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def manacher(s):
    ex = ['#']
    for c in s:
        ex.append(c)
        ex.append('#')

    N = len(ex)
    radius = [1] * N
    rlimit = 0
    axis = 0
    for i in range(1,N):
        if i > rlimit:
            radius[i] = expand_from(ex, i, 1)
            axis = i
            rlimit = i + radius[i] - 1
        else:
            _i = 2 * axis - i
            _r = radius[_i]
            if _i - _r > axis - radius[axis]:
                radius[i] = _r
            elif _i - _r < axis - radius[axis]:
                radius[i] = rlimit - i + 1
            else:
                radius[i] = expand_from(ex, i, rlimit - i + 1)
                axis = i
                rlimit = i + radius[i] - 1

    A = find_max(radius)
    begin = (A - radius[A] + 1) // 2
    _len = radius[A] - 1
    return s[begin:begin+_len]

def find_max(arr):
    i = 0
    for j in range(1,len(arr)):
        if arr[j] > arr[i]:
            i = j
    return i

def expand_from(s, i, init_len):
    L = init_len
    j = i + init_len
    while j < len(s) and i*2-j >= 0 and s[j] == s[i*2-j]:
        j += 1
    return j - i

def palindrome_by_manacher(s):
    ex = ['#']
    for c in s:
        ex.append(c)
        ex.append('#')

    N = len(ex)
    radius = [1] * N
    rlimit = 0
    axis = 0
    for i in range(1,N):
        if i > rlimit:
            r = expand_from(ex, i, 1)
            if i + r - 1 > rlimit:
                axis = i
                rlimit = i + r - 1
                radius[i] = r
                if rlimit == N - 1:
                    break
        else:
            _i = 2 * axis - i
            _r = radius[_i]
            if _i - _r > axis - radius[axis]:
                radius[i] = _r
            elif _i - _r < axis - radius[axis]:
                radius[i] = rlimit - i + 1
            else:
                r = expand_from(ex, i, rlimit - i + 1)
                if i + r - 1 > rlimit:
                    axis = i
                    rlimit = i + r - 1
                    radius[i] = r
                    if rlimit == N - 1:
                        break

    last_len = radius[axis] - 1
    return ''.join(reversed(s[:len(s) - last_len]))

@testwrapper
def test(s):
    print(s)
    print(f'longest palindrome: {manacher(s)}')
    print(palindrome_by_manacher(s))

def main():
    test('222020221')
#    test('12')
#    test('123')
#    test('abc1234321ab')
#    test('abacaba')
#    test('1221')
#    test('CabaddabaC')
#    test('abacabd')
#    test('dabacabac')
#    test('abcd123321')

if __name__ == '__main__':
    main()
