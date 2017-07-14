#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random

def rand_arr(down, up, num):
    a = [random.randint(down, up) for i in range(num)]
    a.sort()
    return a

def k_merge_sort_win(arrs):
    k = len(arrs)
    r = []
    index = [0] * k

    def peek_value(i):
        if index[i] < len(arrs[i]):
            return arrs[i][index[i]]
        else:
            return 0x7fffffff

    def pop_value(i):
        if index[i] < len(arrs[i]):
            v = arrs[i][index[i]]
            index[i] += 1
            return v
        else:
            return 0x7fffffff

    wtree = [0] * k * 2

    def pk(i):
        left = i * 2
        right = left + 1
        L = wtree[left]
        R = wtree[right]
        if peek_value(L) < peek_value(R):
            return L
        else:
            return R

    for i in range(k):
        wtree[i+k] = i

    for i in range(k-1, 0, -1):
        wtree[i] = pk(i)

    while True:
        winner = wtree[1]
        v = pop_value(winner)
        if v == 0x7fffffff:
            break
        r.append(v)
        p = (winner + k) // 2
        while p >= 1:
            wtree[p] = pk(p)
            p = p // 2

    return r

def k_merge_sort_lose(arrs):
    return []

def test(k):
    arrs = []
    for i in range(k):
        n = random.randint(6, 12)
        a = rand_arr(1,100,n)
        arrs.append(a)
        print('[{}] {}'.format(i, a))
    print(k_merge_sort_win(arrs))
    print(k_merge_sort_lose(arrs))
    print()

def main():
    '''分别用胜者树和败者树实现K路归并排序'''
    test(2)
    test(3)
    test(5)
    test(10)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
