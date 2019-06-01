# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------30--')

def sum_of_degrees(n):
    n = str(n)
    res = 0
    for i in range(len(str(n))):
        res = res + int(n[i])**5
    return res


print(sum_of_degrees(1634))

res = 0
for i in range(3, 1_000_000):
    if i == sum_of_degrees(i):
        res = res + i
        print('>', i, res)
    if i % 1_000_000 == 0:
        print(i)

print(res)

