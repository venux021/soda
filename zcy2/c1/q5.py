#!/usr/bin/env python3
import sys

def sort(stk):
    if not stk or len(stk) == 1:
        return

    s2 = []
    while stk:
        while stk and (not s2 or stk[-1] >= s2[-1]):
            s2.append(stk.pop())
        if not stk:
            break
        temp = stk.pop()
        while s2 and s2[-1] > temp:
            stk.append(s2.pop())
        s2.append(temp)

    while s2:
        stk.append(s2.pop())

def test(stk):
    print(stk)
    sort(stk)
    print(stk)
    print('-----')

def main():
    test([1,4,2,7,14,21,8,-1,20,4])
    test([10])
    test([1,2,3,4,5])
    test([5,4,3,2,1])

if __name__ == '__main__':
    main()
