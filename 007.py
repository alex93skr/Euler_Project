# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'-----------------------7--')

def prost(n):
    """простые числа    from prime"""
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False
    return True

limit = 10001

res = 0
n = 1

while not res == limit:
    n += 1
    if prost(n):
        res += 1

print('>>', n, '♥')

