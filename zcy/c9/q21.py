#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def to_zh(num):
    if num == 0:
        return u'零'

    s = []
    is_neg = False
    if num < 0:
        num = -num
        is_neg = True

    a8 = 0
    if num >= 100000000:
        a8 = num / 100000000
        s.append(zh_base(a8))
        s.append(u'亿')
        num %= 100000000

    a4 = 0
    if num >= 10000:
        a4 = num / 10000
        if a8 > 0 and a4 < 1000:
            s.append(u'零')
        s.append(zh_base(a4))
        s.append(u'万')
        num %= 10000
    elif a8 > 0:
        s.append(u'零')

    if a4 > 0 and num < 1000:
        s.append(u'零')
    
    x = zh_base(num)
    if (a8 > 0 or a4 > 0) and x == u'十':
        s.append(u'一')
    s.append(x)

    text =''.join(s)
    if is_neg:
        text = u'负' + text

    return text

def zh_base(k):
    if k == 0:
        return u''

    chars = u'零一二三四五六七八九'

    s = []

    a3 = 0
    if k >= 1000:
        a3 = k / 1000
        s.append(chars[a3])
        s.append(u'千')
        k %= 1000

    if k == 0:
        return ''.join(s)

    a2 = 0
    if k >= 100:
        a2 = k / 100
        s.append(chars[a2])
        s.append(u'百')
        k %= 100
    elif a3 > 0:
        s.append(u'零')

    if k == 0:
        return ''.join(s)

    a1 = 0
    if k >= 10:
        a1 = k / 10
        if a1 != 1 or a3 > 0 or a2 > 0:
            s.append(chars[a1])
        s.append(u'十')
        k %= 10
    elif a2 > 0:
        s.append(u'零')

    if k > 0:
        s.append(chars[k])

    return ''.join(s)


def to_en(num):
    if num == 0:
        return 'zero'

    s = []
    is_neg = False
    if num < 0:
        num = -num
        is_neg = True

    a9 = 0
    if num >= 1000000000:
        a9 = num / 1000000000
        s.append(en_base(a9))
        s.append('Billion,')
        num %= 1000000000

    a6 = 0
    if num >= 1000000:
        a6 = num / 1000000
        s.append(en_base(a6))
        s.append('Million,')
        num %= 1000000

    a3 = 0
    if num >= 1000:
        a3 = num / 1000
        s.append(en_base(a3))
        s.append('Thousand,')
        num %= 1000

    s.append(en_base(num))

    text = ' '.join(s)
    if is_neg:
        text = 'Negative, ' + text

    text = text.strip()

    if text[-1] == ',':
        text = text[:-1]

    return text

def en_base(k):
    if k == 0:
        return ''

    strs = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
    'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
    'Nineteen']

    tens = ['', '', 'Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 
            'Ninety']

    s = []
    a2 = 0
    if k >= 100:
        a2 = k / 100
        s.append(strs[a2])
        s.append('Hundred')
        k %= 100

    a1 = k / 10
    if k >= 20:
        s.append(tens[a1])
        k %= 10

    if a2 > 0 and a1 == 0 and k < 10 and k > 0:
        s.append('and')

    if k > 0:
        s.append(strs[k])

    return ' '.join(s)

def test(num):
    print 'num: {}'.format(num)
    print 'chinese: {}'.format(to_zh(num))
    print 'english: {}'.format(to_en(num))

def main():
    '''数字的英文表达和中文表达'''
    test(1014)
    test(1002)
    test(1000)
    test(200)
    test(103)
    test(234)
    test(23)
    test(13)
    test(8)
    test(10)
    test(12345)
    test(20345)
    test(20040)
    test(120300)
    test(1004567)
    test(1234567)
    test(1030000)
    test(1090002)
    test(50348231)
    test(60002003)
    test(43569000)
    test(534678201)
    test(900003009)
    test(900000010)
    test(-2147483648)
    test(0)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
