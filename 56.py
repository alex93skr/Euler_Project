# !/usr/bin/python3
# -*- coding: utf-8 -*-

print('---------------------- 56 --')

def sum_in_string(st):
    # print(st, len(st))
    st = str(st)
    res = 0
    for i in st:
        # print(i)
        res += int(i)
    # print(res)
    return res

max = 0

for a in range(100):
    for b in range(100):
        tmp = sum_in_string(a ** b)
        if tmp > max:
            max = tmp
        print(a, b, tmp, 'win:', max)

