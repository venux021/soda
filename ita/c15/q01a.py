#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def optimal_assembly_line(fact1, fact2):

    e1, x1, a1, t1 = fact1
    e2, x2, a2, t2 = fact2

    n = len(a1)

    dp1 = [0] * n
    dp2 = [0] * n
    dp1[0] = e1 + a1[0]
    dp2[0] = e2 + a2[0]

    c1 = [0] * n
    c2 = [0] * n

    for i in range(1, n):
        k1 = dp2[i-1] + t2[i-1]
        if k1 < dp1[i-1]:
            c1[i] = 2
            dp1[i] = k1 + a1[i]
        else:
            c1[i] = 1
            dp1[i] = dp1[i-1] + a1[i]

        k2 = dp1[i-1] + t1[i-1]
        if k2 < dp2[i-1]:
            c2[i] = 1
            dp2[i] = k2 + a2[i]
        else:
            c2[i] = 2
            dp2[i] = dp2[i-1] + a2[i]

    C = [None, c1, c2]
    path = []
    if dp1[n-1] + x1 < dp2[n-1] + x2:
        s = 1
    else:
        s = 2
    path.append(s)

    for i in range(n-1, 0, -1):
        s = C[s][i]
        path.append(s)

    return ' '.join(map(lambda x: str(x), path[::-1]))

def test(fact1, fact2):
    print(optimal_assembly_line(fact1, fact2))

def main():
    '''最佳装配线'''
    test((2,3,[7,9,3,4,8,4],[2,3,1,3,4]),
            (4,2,[8,5,6,4,5,7],[2,1,2,2,1]))

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
