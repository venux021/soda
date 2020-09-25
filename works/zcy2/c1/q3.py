#!/usr/bin/env python3
import sys

def reversed_stack(stk):
    if not stk:
        return stk
    bottom = take_bottom(stk)
    reversed_stack(stk)
    stk.append(bottom)

def take_bottom(stk):
    if len(stk) > 1:
        top = stk.pop()
        bottom = take_bottom(stk)
        stk.append(top)
        return bottom
    else:
        return stk.pop()

def test(stk):
    print(stk)
    reversed_stack(stk)
    print(stk)
    print('-----')

def main():
    test([1,2,3,4,5])
    test([1,2])
    test([1])

if __name__ == '__main__':
    main()
