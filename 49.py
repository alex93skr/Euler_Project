# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------49--')


def is_prime(n):        # простые
    if n== 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False
    return True


def same_characters(n1, n2):
    for i in str(n1):
        if i not in str(n2):
            return False
    return True

# 1487, 4817, 8147

for i in range(1000, 10000):
    if is_prime(i) and is_prime(i + 3330) and is_prime(i + 6660):
        # print(i, i + 3330, i + 6660)
        if same_characters(i, i + 3330) and same_characters(i, i + 6660):
            print(i, i + 3330, i + 6660)

# 296962999629

