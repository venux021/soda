#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

digit_en = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
en_10_to_19 = {
    10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
    15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Ninteen'
}
en_decade = {
    20: 'Twenty', 30: 'Thirty', 40: 'Fourty', 50: 'Fifty', 
    60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninty'
}
en_seg = ['', '', 'Thousand', 'Million', 'Billion']

digit_zh = ['零','一','二','三','四','五','六','七','八','九']
zh_seg = ['', '', '万', '亿']

def num_en(num):
    if num == 0:
        return digit_en[num]
    p = num
    if p < 0:
        p = -p
    buf = []
    while p > 0:
        a = p % 1000
        buf.append(a)
        p //= 1000

    k = len(buf)
    buf2 = []
    while k > 0:
        k -= 1
        if buf[k] == 0:
            continue
        buf2.append(tri_to_en(buf[k]).strip() + ' ' + en_seg[k+1])

    buf2 = map(lambda x: x.strip(), buf2)

    return ', '.join(buf2) if num > 0 else ('Negative, ' + ', '.join(buf2))

def tri_to_en(n):
    if n == 0:
        return ''

    r = ''
    if n >= 100:
        r = digit_en[n//100] + ' Hundred '
        n %= 100
    
    if n == 0:
        return r
    elif n >= 10 and n <= 19:
        return r + en_10_to_19[n]
    elif n < 10:
        return r + digit_en[n]
    else:
        return r + en_decade[n//10*10] + ' ' + digit_en[n%10]

def num_zh(num):
    if num == 0:
        return digit_zh[num]
    p = num
    if p < 0:
        p = -p
    buf = []
    while p > 0:
        a = p % 10000
        buf.append(a)
        p //= 10000

    k = len(buf)
    buf2 = []
    while k > 0:
        k -= 1
        if buf[k] == 0:
            continue
        buf2.append(fo_to_zh(buf[k]).strip() + zh_seg[k+1])

    buf2 = map(lambda x: x.strip(), buf2)

    result = ''.join(buf2)
    if num < 0:
        result = '负' + result
    return result

def fo_to_zh(n):
    if n == 0:
        return ''

    i4 = n // 1000
    i3 = (n // 100) % 10
    i2 = (n // 10) % 10
    i1 = n % 10

    r = ''
    if i4 > 0:
        r = digit_zh[i4] + '千'
    if i3 > 0:
        r += digit_zh[i3] + '百'
    if i2 > 0:
        if i4 > 0 and i3 == 0:
            r += '零'
            if i2 > 1:
                r += digit_zh[i2] + '十'
            else:
                r += '十'
        else:
            r += digit_zh[i2] + '十'
    if i1 > 0:
        if (i3 > 0 or i4 > 0) and i2 == 0:
            r += '零'
        r += digit_zh[i1]
    return r

@testwrapper
def test(num):
    print(num)
    print(num_en(num))
    print(num_zh(num))

def main():
    test(319)
    test(1014)
    test(65537)
    test(538729)
    test(4208710)
    test(4200000)
    test(4200900)
    test(4200002)
    test(23456789)
    test(23000789)
    test(-2147483648)
    test(0)

if __name__ == '__main__':
    main()
