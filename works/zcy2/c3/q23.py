#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def count_tree(nodes):
    n = len(nodes)
    arr = [1] * (n+1)
    for i in range(2, n+1):
        c = 0
        for j in range(0, i):
            c += (arr[j] * arr[i-1-j])
        arr[i] = c
    counts = {}
    for i, v in enumerate(nodes):
        L = i
        R = n - i - 1
        k = arr[L] * arr[R]
        counts[v] = k
    return arr[n], counts

@testwrapper
def test(total):
    nodes = [i+1 for i in range(total)]
    n, counts = count_tree(nodes)
    print(f'total: {n}')
    print(counts)

def main():
    test(2)
    test(3)
    test(5)
    test(10)

if __name__ == '__main__':
    main()
