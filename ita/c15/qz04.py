#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random

MAX = sys.maxsize

def format_print(words, line_size):
    n = len(words)
    dp = [0] * n
    line_ends = [n-1] * n

    length = [0] * (n+1)
    for i in range(n):
        length[i] = length[i-1] + len(words[i])

    for i in range(n-2, -1, -1):
        dp[i] = MAX
        for j in range(i, n):
            b = line_size - j + i - (length[j] - length[i-1])
            if b < 0:
                break
            if j < n-1:
                b = pow(b, 3) + dp[j+1]
            else:
                b = 0
            if dp[i] > b:
                dp[i] = b
                line_ends[i] = j

    p = 0
    while p < n:
        i = p
        j = line_ends[p]
        trail_blanks = line_size - j + i - (length[j] - length[i-1])
        for k in range(i, j):
            print(words[k], end = ' ')
        print(words[j], end = '')
        for z in range(trail_blanks):
            print(' ', end = '')
        print('[{}]'.format(trail_blanks))
        p = j + 1

    print('total price:', dp[0])

def test(num_words, line_size):
    words = gen_words(num_words)
    format_print(words, line_size)

def main():
    '''整齐打印问题'''
    test(100, 20)
    format_print(['street', 'fight', 'one', 'boy'], 10)

def gen_words(num):
    words = []
    for i in range(num):
        L = random.randint(1,7)
        w = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for j in range(L)])
        words.append(w)
    return words

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
