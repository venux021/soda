#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random

from q02a import show_optimal_greedy

class Node:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.uprice = value // weight

def show_optimal_linear(capacity, weight, value):
    n = len(weight)
    objs = [Node(weight[i], value[i]) for i in range(n)]

    i = 0
    j = n-1
    total_value = 0
    print('for linear algorithm')
    while True:
        mid = (j+j) // 2
        pivot = kth_element(objs, i, j, mid).uprice
        low = i-1
        high = j+1
        k = 0
        while k < high:
            if objs[k].uprice == pivot:
                k += 1
            elif objs[k].uprice > pivot:
                low += 1
                swap(objs, low, k)
                k += 1
            else:
                high -= 1
                swap(objs, k, high)
        # [i:low+1] < piv, [low+1:k] == piv, [k:j+1] > piv
        
        W1 = weight_sum(objs, i, low)
        W2 = weight_sum(objs, low+1, k-1)
        W3 = weight_sum(objs, k, j)
        if W1 > capacity:
            j = low
        elif W1 + W2 >= capacity:
            total_value = value_sum(objs, i, low)
            for y in range(i, low+1):
                print('u:{} w:{} t:{}'.format(
                            objs[y].uprice, objs[y].weight, objs[y].weight))

            total_value += (capacity - W1) * objs[low+1].uprice
            C = capacity - W1
            for y in range(low+1, k):
                if objs[y].weight <= C:
                    print('u:{} w:{} t:{}'.format(
                                objs[y].uprice, objs[y].weight, objs[y].weight))
                else:
                    print('u:{} w:{} t:{}'.format(
                                objs[y].uprice, objs[y].weight, C))
                    break
                C -= objs[y].weight
            break
        else:
            total_value += value_sum(objs, i, k-1)
            for y in range(i, k):
                print('u:{} w:{} t:{}'.format(
                            objs[y].uprice, objs[y].weight, objs[y].weight))
            capacity -= (W1+W2)
            i = high
    print('Linear algorithm:', total_value)

def weight_sum(objs, i, j):
    return sum(map(lambda x: x.weight, objs[i:j+1]))

def value_sum(objs, i, j):
    return sum(map(lambda x: x.value, objs[i:j+1]))

def insertion_sort(objs, i, j):
    for s in range(i, j):
        e = s + 1
        t = objs[e]
        while e > s and objs[e-1].uprice < t.uprice:
            objs[e] = objs[e-1]
            e -= 1
        objs[e] = t

def kth_element(objs, i, j, k):
    if j - i < 3:
        insertion_sort(objs, i, j)
        return objs[k]

    m_median = median_median(objs, i, j)
    pivot = m_median.uprice

    low = i - 1
    high = j + 1
    m = i
    while m < high:
        if objs[m].uprice == pivot:
            m += 1
        elif objs[m].uprice > pivot:
            low += 1
            swap(objs, m, low)
            m += 1
        else:
            high -= 1
            swap(objs, m, high)
    if k > low and k < m:
        return objs[k]
    elif k <= low:
        return kth_element(objs, i, low, k)
    else:
        return kth_element(objs, m, j, k)

def median_median(objs, i, j):
    n = j - i + 1
    num_median = n // 5
    if n % 5 > 0:
        num_median += 1

    medians = [0] * num_median

    for y in range(i, j+1, 5):
        e = min(y+4, j)
        insertion_sort(objs, y, e)
        if (e-y) & 1 == 1:
            medians[(y-i)//5] = objs[(y+e)//2+1]
        else:
            medians[(y-i)//5] = objs[(y+e)//2]

    return kth_element(medians, 0, num_median-1, (num_median-1)//2)

def kth_element2(objs, i, j, k):
    if j - i < 3:
        insertion_sort(objs, i, j)
        return objs[k]

    piv = get_pivot(objs, i, j)
    low = i
    high = j - 1
    while True:
        low += 1
        while objs[low].uprice > piv:
            low += 1
        high -= 1
        while objs[high].uprice < piv:
            high -= 1
        if low < high:
            swap(objs, low, high)
        else:
            break
    swap(objs, low, j)
    p = low

    if p == k:
        return objs[p]
    elif p > k:
        return kth_element(objs, i, p-1, k)
    else:
        return kth_element(objs, p+1, j, k)

def get_pivot(objs, i, j):
    mid = (i+j)//2
    if objs[i].uprice < objs[j].uprice:
        swap(objs, i, j)
    if objs[i].uprice < objs[mid].uprice:
        swap(objs, i, mid)
    if objs[mid].uprice < objs[j].uprice:
        swap(objs, mid, j)
    swap(objs, j, j-1)
    swap(objs, j, mid)
    return objs[j].uprice

def swap(objs, i, j):
    t = objs[i]
    objs[i] = objs[j]
    objs[j] = t

def test(n):
    uprice = [random.randint(1,10) for i in range(n)]
    weight = [random.randint(5,35) for i in range(n)]
    value = [uprice[i] * weight[i] for i in range(n)]
    capacity = sum(weight) * 6 // 7
    show_optimal_greedy(capacity, weight, value)
    show_optimal_linear(capacity, weight, value)

def main():
    '''O(n)时间求解分数背包问题'''
    test(2)
    test(20)
    test(50)
    test(100)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
