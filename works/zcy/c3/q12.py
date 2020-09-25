#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from bitree import *

def has_sub(t1, t2):
    seq1 = serialize(t1)
    seq2 = serialize(t2)

    nextval = get_next(seq2)

    i = j = 0
    while i < len(seq1) and j < len(seq2):
        if j == -1:
            j = 0
            i += 1
        elif seq1[i] == seq2[j]:
            i += 1
            j += 1
        else:
            j = nextval[j]

    return j == len(seq2)

def serialize(tree):
    seq = []
    do_serial(tree, seq)
    return ''.join(seq)

def do_serial(tree, seq):
    if not tree:
        seq.append('#!')
        return
    seq.append('{}!'.format(tree.str_val()))
    do_serial(tree.left, seq)
    do_serial(tree.right, seq)

def get_next(s):
    n = len(s)
    nextv = [0] * n
    nextv[0] = -1
    j = -1
    i = 1
    while i < n:
        if j == -1 or s[j] == s[i-1]:
            j += 1
            nextv[i] = j
            i += 1
        else:
            j = nextv[j]
    return nextv

def test(s1, s2):
    t1 = parse_bitree(s1)
    t2 = parse_bitree(s2)
    print(has_sub(t1, t2))

def main():
    '''判断t1树中是否有与t2树拓扑结构完全相同的子树'''
    test('1 2 3 4 5 6 7 ## 8 9', '2 4 5 ## 8 9')
    test('1 2 3 4 5 6 7 ## 8 9', '2 4 5 ## 8')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
