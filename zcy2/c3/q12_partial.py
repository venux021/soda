#!/usr/bin/env python3
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def build_next(match):
    inext = [None] * len(match)
    nextval = [-1] * len(match)
    inext[0] = nextval[0] = -1
    for i in range(1, len(match)):
        j = inext[i-1]
        while j > -1 and match[j] != match[i-1]:
            j = inext[j]
        inext[i] = j + 1
        if match[i] != match[j+1]:
            nextval[i] = j + 1
        else:
            nextval[i] = nextval[j+1]
        #if match[i] != match[j+1]:
        #    inext[i] = j + 1
        #else:
        #    inext[i] = inext[j+1]
#    return inext
    return nextval

@testwrapper
def test(s1, s2):
    pass

def main():
    print(build_next('aaaab'))
    print(build_next('abc1abc1'))
    print(build_next('abc1abc2'))

if __name__ == '__main__':
    main()
