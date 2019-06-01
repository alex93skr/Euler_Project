# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------39--')


import math


# 120
# {20,48,52}, {24,45,51}, {30,40,50}
# P = a + b + c
# c2 = a2 + b2


# print(20 ** 2 + 48 ** 2, 52 ** 2)
# print(24 ** 2 + 45 ** 2, 51 ** 2)
# print(30 ** 2 + 40 ** 2, 50 ** 2)

lim = 1001
# 465 0     winner: 5 for 420

res_max = 0
res_max_data = []

for p in range(1, lim):
    # print(p)
    res = 0
    for c in range(1, p):
        for b in range(1, c):
            # a = 1
            # while a + b + c <= p:
            # for a in range(1, p - c -b):
            for a in range(1, b):
                if a + b + c == p and c ** 2 == a ** 2 + b ** 2:
                    res += 1
                    print('>', p, '=', a,b,c)


    if res > res_max:
        res_max = res
        res_max_data = p

    print('>>', p, int(res), '    winner:', res_max, 'for', res_max_data)

print(res_max, 'for', res_max_data)


# ------

import time
from collections import Counter

# startTime = time.clock()

MAX = 1000

def getB(p, a):
    return (p ** 2 - 2 * p * a) // (2 * p - 2 * a)

triangleSolutions = [(p, a, getB(p, a), p - a - getB(p, a)) for p in range(2, MAX + 1, 2) for a in range(1, p // 3 + 1)  if a ** 2 + getB(p, a) ** 2 == (p - a - getB(p, a)) ** 2]

perimeters = [x[0] for x in triangleSolutions]

maximized = Counter(perimeters).most_common()[0][0]

print("The right-triangle perimeter below {0} with the most solutions is {1}.".format(MAX, maximized))

# print("Program execution took {0} seconds.".format(time.clock() - startTime))


