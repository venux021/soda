#!/usr/bin/env python3
import random
import sys

from sodacomm.tools import testwrapper

def rand_1toM(m):
    return int(random.random() * m) + 1

def rand_1toN(m, n):
    if m >= n:
        while True:
            r = rand_1toM(m)
            if r <= n:
                return r
    k = 1
    while pow(m, k) < n:
        k += 1

    j = int(pow(m, k)) // n
    z = n * j
    while True:
        s = 0
        for i in range(k):
            s = s * m + (rand_1toM(m)-1)
        if s < z:
            return s % n + 1

@testwrapper
def test3(_m, n):
    print(_m, n)
    m = {}
    total = 1000 * n
    for i in range(total):
        r = rand_1toN(_m, n)
        m[r] = m.get(r,0) + 1
    print([(v, f'{p/total:.3f}') for v, p in m.items()])

def random_1to5():
    return int(random.random() * 5) + 1

def random_1to7():
    while True:
        r = (random_1to5()-1) * 5 + (random_1to5()-1)
        if r <= 20:
            return r % 7 + 1

@testwrapper
def test1():
    m = {}
    total = 7777
    for i in range(total):
        r = random_1to7()
        m[r] = m.get(r,0) + 1
    print([(v, f'{p/total:.3f}') for v, p in m.items()])

def random01p():
    p = 0.83
    r = random.random()
    if r < 0.83:
        return 0
    else:
        return 1

def rand01():
    while True:
        a = random01p()
        b = random01p()
        if a != b:
            return b

def random_1to6():
    while True:
        a = rand01()
        b = rand01()
        c = rand01()
        k = a * 4 + b * 2 + c
        if k <= 5:
            return k + 1

@testwrapper
def test2():
    m = {}
    total = 6666
    for i in range(total):
        r = random_1to6()
        m[r] = m.get(r,0) + 1
    print([(v, f'{p/total:.3f}') for v, p in m.items()])

def main():
    test1()
    test2()
    test3(6, 4)
    test3(6, 6)
    test3(8, 13)
    test3(3, 30)

if __name__ == '__main__':
    main()
