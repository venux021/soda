# -*- coding: utf-8 -*-
import sys

MAX = 0x7fffffff

def min_money(arr, aim):
    if aim <= 0:
        return 0
    dp = [[0] * (aim+1) for i in range(0, len(arr))]
    
    for i in range(aim+1):
        dp[0][i] = MAX

    i = j = 0
    while i < (aim+1):
        dp[0][i] = j
        j += 1
        i += arr[0]

    for i in range(1, len(arr)):
        for j in range(1, aim+1):
            a = dp[i-1][j]
            if j - arr[i] >= 0:
                b = dp[i][j-arr[i]] + 1
                dp[i][j] = min(a,b)
            else:
                dp[i][j] = a
    r = dp[len(arr)-1][aim]
    return r if r < MAX else -1

def min_money2(arr, aim):
    if aim <= 0:
        return 0

    R = len(arr)
    C = aim + 1
    dp = [MAX] * C

    i = j = 0
    while i < (aim+1):
        dp[i] = j
        j += 1
        i += arr[0]

    for i in range(1, R):
        for j in range(1, C):
            if j - arr[i] >= 0:
                b = dp[j-arr[i]] + 1
                dp[j] = min(dp[j], b)
    r = dp[C-1]
    return r if r < MAX else -1 

def test(arr, aim):
    print 'arr: {}'.format(arr)
    print 'aim: {}'.format(aim)
    print min_money(arr, aim)
    print min_money2(arr, aim)

def main():
    '''换钱最少货币数
'''
    test([5,2,3], 20)
    test([5,2,3], 0)
    test([3,5], 2)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()

