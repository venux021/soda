#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def max_sum_matrix(mx):
    R = len(mx)
    C = len(mx[0])
    _max = -sys.maxsize
    for i in range(R):
        s = [0] * C
        for j in range(i, R):
            cur = 0
            for k in range(C):
                s[k] += mx[j][k]
                cur += s[k]
                _max = max(_max, cur)
                if cur < 0:
                    cur = 0
    return _max

@testwrapper
def test(mx):
    print(mx)
    print(max_sum_matrix(mx))

def main():
    test([[-90,48,78],[64,-40,64],[-81,-7,66]])
    test([[-1,-1,-1],[-1,2,2],[-1,-1,-1]])
    test([[-2,3,-5,7],[1,4,-1,-3]])

if __name__ == '__main__':
    main()
