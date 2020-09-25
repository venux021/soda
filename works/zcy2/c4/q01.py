#!/usr/bin/env python3
import itertools
import sys

from sodacomm.tools import testwrapper

def matrix_pow(mx, n):
    p = 1
    if p & n:
        r = mx
    else:
        r = unit_matrix(mx)
    k = mx
    while True:
        p = p << 1
        if p > n:
            break
        k = matrix_multiply(k, k)
        if p & n:
            r = matrix_multiply(r, k)
    return r

def unit_matrix(mx):
    u = [[0] * len(mx) for _ in range(len(mx))]
    for i in range(len(mx)):
        u[i][i] = 1
    return u

def matrix_multiply(m1, m2):
    col = len(m2[0])
    row = len(m1)
    c = len(m1[0])
    r = [[0] * col for _ in range(row)]
    for i, j, k in itertools.product(range(row), range(col), range(c)):
        r[i][j] += m1[i][k] * m2[k][j]
    return r

def feb(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    p = matrix_pow([[1,1],[1,0]], n-2)
    r = matrix_multiply([[1,1]], p)
    return r[0][0]

def cow(n):
    if n < 4:
        return n
    p = matrix_pow([[1,1,0],[0,0,1],[1,0,0]], n-3)
    r = matrix_multiply([[3,2,1]], p)
    return r[0][0]

@testwrapper
def test(n):
    print(f'Feb[{n}] = {feb(n)}')
    print(f'Cow[{n}] = {cow(n)}')

def main():
    test(3)
    test(4)
    test(5)
    test(6)
    test(10)
    test(11)
    test(17)

if __name__ == '__main__':
    main()
