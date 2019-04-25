#!/usr/bin/env python3
import random
import sys

from sodacomm.tools import testwrapper

def keep_k(k, total):
    if total <= 0:
        return []
    elif total <= k:
        return [i+1 for i in range(total)]

    bag = [i+1 for i in range(k)]
    for i in range(k+1, total+1):
        if rand(i) <= k:
            bag[rand(k)-1] = i

    return bag

def rand(mx):
    return int(random.random() * mx) + 1

@testwrapper
def test(k, total):
    print(k, total)
    print(keep_k(k, total))

def main():
    test(10, 5)
    test(10, 10)
    test(10, 100)
    test(10, 1000)

if __name__ == '__main__':
    main()
