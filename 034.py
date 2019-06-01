# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------34--')

import math

def fac_sum(n):
    tmp = 0
    for i in str(n):
        tmp += math.factorial(int(i))
    return tmp

for i in range(3, 100000000):
    if i == fac_sum(i):
        print(i)
    if i % 100_000 == 0:
        print('>', i)


