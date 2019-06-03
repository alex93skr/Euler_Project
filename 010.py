# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------10--')


def is_prime(n):
    """простые числа    from prime"""
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False
    return True



n = 0
for i in range(2, 2_000_001):
    if is_prime(i):
        n += i
        print(i, n)

print(n)
