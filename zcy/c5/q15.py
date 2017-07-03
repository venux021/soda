#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

NUM = 0
OP = 1

class Token(object):

    def __init__(self, _type, value):
        self._type = _type
        if _type == NUM:
            self.num = value
        else:
            self.op = value

def is_num(char):
    return char >= '0' and char <= '9'

def dump(tokens):
    for t in tokens:
        if t._type == NUM:
            print 'num ', t.num
        else:
            print 'op  ', t.op

def cal(expr):
    n = len(expr)
    tokens = []
    i = 0
    while i < n:
        if is_num(expr[i]):
            j = i
            while j < n and expr[j] >= '0' and expr[j] <= '9':
                j += 1
            tokens.append(Token(NUM, int(expr[i:j])))
            i = j
        else:
            tokens.append(Token(OP, expr[i]))
            i += 1

    tokens.append(Token(OP, '#'))

    i = 0
    numstk = []
    opstk = ['#']

    while len(opstk) > 0:
        tk = tokens[i]
        if tk._type == NUM:
            numstk.append(tk.num)
            i += 1
        else:
            top = opstk[-1]
            c = do_cmp(top, tk.op)
            if c == 1:
                numstk[-2] = calculate(numstk[-2], top, numstk[-1])
                del opstk[-1]
                del numstk[-1]
            elif c == 0:
                del opstk[-1]
                i += 1
            elif c == -1:
                opstk.append(tk.op)
                i += 1
            else:
                print 'error: {} {}'.format(top, tk.op)
                return

    return numstk[0]

def do_cmp(op1, op2):
    i = op_index(op1)
    j = op_index(op2)
    return PRI_MX[i][j]

OPS = '+-*/()#'
OPINDEX = {}
for i, c in enumerate(OPS):
    OPINDEX[c] = i
PRI_MX = [
    [ 1, 1,-1,-1,-1, 1, 1],
    [ 1, 1,-1,-1,-1, 1, 1],
    [ 1, 1, 1, 1,-1, 1, 1],
    [ 1, 1, 1, 1,-1, 1, 1],
    [-1,-1,-1,-1,-1, 0,-2],
    [-2,-2,-2,-2,-2,-2,-2],
    [-1,-1,-1,-1,-1,-2, 0]
]

def op_index(op):
    return OPINDEX[op]

def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        print 'error'


def test(expr):
    print 'expr: {}'.format(expr)
    print 'val: {}'.format(cal(expr))

def main():
    '''公式字符串求值'''
    test('48*((70-65)-43)+8*1')
    test('3+1*4')
    test('3+(1*4)')
    test('36/((1+2)*3)-((3+2)*2)')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
