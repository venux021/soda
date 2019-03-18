#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def count_bool(s, b):
    ds = s[::2]
    op = s[1::2]
    n = len(ds)
    assert len(op) == n - 1
    mtrue = [[0] * n for _ in range(n)]
    mfalse = [[0] * n for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        if ds[i] == '1':
            mtrue[i][i] = 1
        else:
            mfalse[i][i] = 1
        dp[i][i] = mtrue[i][i] if b else mfalse[i][i]
    for k in range(2, n+1):
        for i in range(n-k+1):
            true_count = false_count = 0
            for j in range(i+1, i+k):
                _op = op[j-1]
                if _op == '&':
                    c_true = mtrue[i][j-1] * mtrue[j][i+k-1]
                    c_false = (mtrue[i][j-1] + mfalse[i][j-1]) * mfalse[j][i+k-1] + mfalse[i][j-1] * mtrue[j][i+k-1]
                elif _op == '|':
                    c_true = (mtrue[i][j-1] + mfalse[i][j-1]) * mtrue[j][i+k-1] + mtrue[i][j-1] * mfalse[j][i+k-1]
                    c_false = mfalse[i][j-1] * mfalse[j][i+k-1]
                else:
                    c_true = mtrue[i][j-1] * mfalse[j][i+k-1] + mfalse[i][j-1] * mtrue[j][i+k-1]
                    c_false = mtrue[i][j-1] * mtrue[j][i+k-1] + mfalse[i][j-1] * mfalse[j][i+k-1]
                true_count += c_true
                false_count += c_false
            mtrue[i][i+k-1] = true_count
            mfalse[i][i+k-1] = false_count
            if b:
                dp[i][i+k-1] = true_count
            else:
                dp[i][i+k-1] = false_count

    return dp[0][n-1]

@testwrapper
def test(ex, de):
    print(ex, de)
    print(count_bool(ex, de))

def main():
    test('1^0|0|1', False)
    test('1^0|0|1', True)
    test('1^0&0|1', True)
    test('1^0&0|1', False)
    test('1^0|0&1^1&0|1', True)
    test('1^0|0&1^1&0|1', False)

if __name__ == '__main__':
    main()
