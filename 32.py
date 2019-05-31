# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------32--')





from itertools import permutations      # все возможные перестановки ПЕРЕБОР

res = 0
prz = []

def check_multipliers(n):
    global res, prz
    # print(n)
    n = str(n)
    for i in range(1, len(n)-1):
        for j in range(i+1, len(n)):
            if int(n[:i]) * int(n[i:j]) == int(n[j:]):
                # print(i, '>', n[:i], n[i:j], n[j:])
                print(n[:i] + '*' + n[i:j] + '=' + n[j:])
                prz += [int(n[j:])]
                # return n[:i] + '*' + n[i:j] + '=' + n[j:]


a = [*'123456789']
n = len(a)
rep = 1
for i in permutations(a * rep, n):
    tmp = int(''.join(i))
    check_multipliers(tmp)
    # if not check_multipliers(tmp) == None:
    #     print(check_multipliers(tmp))

print(prz)
prz = list(set(prz))
print(prz)
import numpy

print('>>>', numpy.sum(prz))


