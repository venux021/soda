#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def stat(s, k):
    if k < 0:
        return None
    t = 0
    arr = s.split('_')
    for i in range(1, len(arr), 2):
        t += int(arr[i])
        if t > k:
            return arr[i-1]
    return None

def test(s, k):
    print 's: {}, k: {}'.format(s, k)
    print 'stat: {}'.format(stat(s, k))

def main():
    '''字符串的统计字符串'''
    test('a_1_b_100', 0)
    test('a_3_b_2_a_1_d_3_f_2_c_1', 3)
    test('a_3_b_2_a_1_d_3_f_2_c_1', 5)
    test('a_3_b_2_a_1_d_3_f_2_c_1', 10)
    test('a_3_b_2_a_1_d_3_f_2_c_1', 100)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
