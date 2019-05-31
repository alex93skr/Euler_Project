# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------25--')



fib1, fib2 = 0, 1
n = 0

while len(str(fib1)) != 1000:
    tmp = fib1 + fib2
    fib1 = fib2
    fib2 = tmp
    n += 1
    print(n, fib1)


