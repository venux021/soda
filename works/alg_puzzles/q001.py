#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

objects = [None, 'wolf', 'sheep', 'vegetable']

def wolf_sheep_veg():
    # -1:man, 1:wolf, 2:sheep, 3:vegetable
    left_bank = [None, 1, None, 3]
    right_bank = [None,None,None,None]
    path = ['move right with sheep']
    do_wsv('right', left_bank, right_bank, boat = [-1, 2], path = path)
    return path

def do_wsv(move, left_bank, right_bank, boat, path):
    if move == 'right' and not any(left_bank):
        right_bank[0] = -1
        right_bank[boat[1]] = boat[1]
        boat[:] = [None,None]
        return True

    carry = boat[1]

    if move == 'right':
        if carry:
            right_bank[carry] = carry
            boat[1] = None
            if is_safe(right_bank):
                path.append('move left')
                if do_wsv('left', left_bank, right_bank, boat, path):
                    return True
                path.pop()
        for i in range(1,4):
            if right_bank[i] and i != carry:
                boat[1] = i
                right_bank[i] = None
                if is_safe(right_bank):
                    path.append(f'move left with {objects[i]}')
                    if do_wsv('left', left_bank, right_bank, boat, path):
                        return True
                    path.pop()
                boat[1] = None
                right_bank[i] = i
    else:
        if carry:
            left_bank[carry] = carry
            boat[1] = None
            if is_safe(left_bank):
                path.append('move right')
                if do_wsv('right', left_bank, right_bank, boat, path):
                    return True
                path.pop()
        for i in range(1,4):
            if left_bank[i] and i != carry:
                boat[1] = i
                left_bank[i] = None
                if is_safe(left_bank):
                    path.append(f'move right with {objects[i]}')
                    if do_wsv('right', left_bank, right_bank, boat, path):
                        return True
                    path.pop()
                boat[1] = None
                left_bank[i] = i

    return False

def is_safe(bank):
    if bank[0]:
        return True
    for i in range(1,len(bank)-1):
        if bank[i] and bank[i+1]:
            return False
    return True

@testwrapper
def test():
    steps = wolf_sheep_veg()
    for s in steps:
        print(s)

def main():
    test()

if __name__ == '__main__':
    main()
