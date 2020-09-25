#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random

MAX_ITER = 100000

def rand5():
    return int(random.random() * 5) + 1

def rand7():
    i = 21
    while i >= 21:
        a = rand5() - 1
        b = rand5() - 1
        i = a * 5 + b
    return i % 7 + 1

def rand01p():
    p = 0.83
    return 0 if random.random() < p else 1

def rand01():
    while True:
        a = rand01p()
        b = rand01p()
        if a != b:
            return a

def rand0to7():
    a = rand01() * 4
    b = rand01() * 2
    c = rand01()
    return a + b + c

def rand1to6():
    num = rand0to7()
    while num >= 6:
        num = rand0to7()
    return num + 1

def test(rand_func, n):
    mc = {}
    print '1 - {}'.format(n)
    iter_times = MAX_ITER * n
    for i in xrange(iter_times):
        r = rand_func()
        mc[r] = mc.get(r, 0) + 1
    for k, v in mc.items():
        ratio = float(v) / iter_times
        print k, ratio
    print '------------------------'

def rand_m(m):
    return int(random.random() * m) + 1

def magic_distrib(m, n):
    def func():
        k = 1
        s = m
        while s < n:
            s *= m
            k += 1
        t = s / n
        bound = t * n
        nums = [0] * k
        while True:
            for i in range(k):
                nums[i] = rand_m(m) - 1
            s = 0
            for i in range(k):
                s *= m
                s += nums[i]
            if s < bound:
                return s % n + 1
    return func

def main():
    '''从5随机到7随机及其扩展'''
    test(rand7, 7)
    test(rand1to6, 6)
    test(magic_distrib(5, 7), 7)
    test(magic_distrib(7, 67), 67)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
