#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random

MAX = sys.maxsize

def find_path_recur(matrix):
    _min = MAX
    col_size = len(matrix[0])
    for i in range(col_size):
        _min = min(_min, _fpr(matrix, 0, i))
    return _min

def _fpr(mx, row, col):
    if row >= len(mx):
        return 0

    col_size = len(mx[row])
    if col == 0:
        return min(mx[row][col] + _fpr(mx,row+1,col), mx[row][col] + _fpr(mx,row+1,col+1))
    elif col == col_size - 1:
        return min(mx[row][col] + _fpr(mx,row+1,col), mx[row][col] + _fpr(mx,row+1,col-1))
    else:
        return min(mx[row][col] + _fpr(mx,row+1,col), mx[row][col] + _fpr(mx,row+1,col+1), mx[row][col] + _fpr(mx,row+1,col-1))


def find_path(matrix):
    row = len(matrix)
    col = len(matrix[0])
    
    dp_last = [0] * col
    dp_cur = [0] * col
    path = [[-1] * col for i in range(row)]
    for j in range(col):
        dp_last[j] = matrix[0][j]

    for i in range(1, row):
        dp = dp_last
        print(dp)
        for j in range(0, col):
            M = matrix[i][j]
            if j == 0:
                if dp[j] < dp[j+1]:
                    path[i][j] = j
                else:
                    path[i][j] = j+1
                dp_cur[j] = min(dp[j], dp[j+1]) + M
            elif j == col-1:
                if dp[j] < dp[j-1]:
                    path[i][j] = j
                else:
                    path[i][j] = j-1
                dp_cur[j] = min(dp[j], dp[j-1]) + M
            else:
                a = dp[j-1]
                b = dp[j]
                c = dp[j+1]
                if a < c:
                    if a < b:
                        path[i][j] = j-1
                    else:
                        path[i][j] = j
                else:
                    if c < b:
                        path[i][j] = j+1
                    else:
                        path[i][j] = j
                dp_cur[j] = min(dp[j-1], dp[j], dp[j+1]) + M
        t = dp_last
        dp_last = dp_cur
        dp_cur = t

    dp_cur = dp_last
    print(dp_cur)
    min_i = 0
    for j in range(1, col):
        if dp_cur[j] < dp_cur[min_i]:
            min_i = j

    p = min_i
    i = row-1
    r = []
    while p >= 0:
        r.append((i, p))
        p = path[i][p]
        i -= 1

    r = r[::-1]
    for i, j in r:
        for index, value in enumerate(matrix[i]):
            if index != j:
                print('* ', end = ' ')
            else:
                print(matrix[i][j], end = ' ')
        print()

    return min(dp_cur)


def test(m, n):
    matrix = [[random.randint(10,99) for i in range(n)] for j in range(m)]
#    matrix = [[85, 15], [16, 40]]
#    matrix = [[80, 32, 45, 81, 37], [87, 92, 50, 99, 64], [36, 55, 35, 96, 49], [87, 69, 22, 57, 65], [24, 26, 61, 83, 35]]
    print('non recursive:', find_path(matrix))
    if m < 13:
        print('recursive:', find_path_recur(matrix))
    print('--------')

def main():
    '''基于接缝裁剪的图像压缩'''
    test(5,5)
    test(10, 13)
    test(11, 18)
    test(12, 18)
    test(13, 18)
    test(20, 23)
    test(50, 53)
    test(100, 103)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()

