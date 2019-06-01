# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------24--')

from itertools import permutations


a = ('0','1','2')
a = ('0','1','2','3','4','5','6','7','8','9')
n = len(a)
rep = 1


res = 1

for i in permutations(a * rep, n):
    tmp = ''.join(i)
    print(tmp, res)
    if res == 1_000_000:
        quit()
    res += 1


