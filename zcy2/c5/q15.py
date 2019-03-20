#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def evaluate_expr(s):
    nbuf = []
    neg = False
    token = []
    for i, c in enumerate(s):
        if c in '0123456789':
            nbuf.append(c)
        elif c == '-':
            if i == 0 or s[i-1] not in '0123456789)':
                neg = True
            else:
                if nbuf:
                    token.append(parse_int(nbuf, neg))
                    neg = False
                    nbuf.clear()
                token.append('-')
        else:
            if nbuf:
                token.append(parse_int(nbuf, neg))
                neg = False
                nbuf.clear()
            token.append(c)

    if nbuf:
        token.append(parse_int(nbuf, neg))

    print(token)

    token.append('#')
    opstk = ['#']
    numstk = []
    for t in token:
        if isinstance(t, int):
            numstk.append(t)
        else:
            while True:
                c = opcmp(opstk[-1], t)
                if c > 0:
                    n2 = numstk.pop()
                    n1 = numstk[-1]
                    op = opstk.pop()
                    numstk[-1] = calculate(n1, op, n2)
                elif c < 0:
                    opstk.append(t)
                    break
                else:
                    opstk.pop()
                    break
    return numstk[0]

def opcmp(op1, op2):
    idx = {c:i for i,c in enumerate('+-*/()#')}
    mx = [
        # +  -  *  /  (  ) '#'
        [ 1, 1,-1,-1,-1, 1, 1], # +
        [ 1, 1,-1,-1,-1, 1, 1], # -
        [ 1, 1, 1, 1,-1, 1, 1], # *
        [ 1, 1, 1, 1,-1, 1, 1], # /
        [-1,-1,-1,-1,-1, 0,-2], # (
        [ 1, 1, 1, 1,-2,-2, 1], # )
        [-1,-1,-1,-1,-1,-1, 0], # '#'
    ]
    i1 = idx[op1]
    i2 = idx[op2]
    return mx[i1][i2]

def calculate(n1, op, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    else:
        raise Exception(f'Unsupported op: {op}')

def parse_int(nbuf, neg):
    n = 0
    for c in nbuf:
        n = n * 10 + (ord(c) - ord('0'))
    return n if not neg else -n

@testwrapper
def test(s):
    print(s)
    print(evaluate_expr(s))
    print(eval(f'print({s})'))

def main():
    test('1+2')
    test('48*((70-65)-43)+8*1')
    test('-48*((70-65)-43)+8*1')
    test('48*((-70-65)-43)+8*1')
    test('48*((-70-65)-(-43))+8*1')

if __name__ == '__main__':
    main()
