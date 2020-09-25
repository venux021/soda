#!/usr/bin/env python3
import sys

def reverse_stack(stk):
    if stk:
        bottom = remove_bottom(stk)
        reverse_stack(stk)
        stk.append(bottom)

def remove_bottom(stk):
    if len(stk) == 1:
        return stk.pop()
    else:
        top = stk.pop()
        bottom = remove_bottom(stk)
        stk.append(top)
        return bottom

def test(stk):
    print(f'origin: {stk}')
    reverse_stack(stk)
    print(f'reversed: {stk}')
    print('----')

def main():
    test([1,2,3,4,5])
    test([1])
    test([1,2])

if __name__ == '__main__':
    main()
