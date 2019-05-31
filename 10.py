# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------10--')


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


n = 0
for i in range(2, 2_000_000):
    if isPrime(i):
        n += i
        print(i, n)

