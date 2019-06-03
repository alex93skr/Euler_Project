# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------9--')


# import functools


def triplet(n, m):
    return [m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2]


res = [triplet(i, j) for i in range(100) for j in range(i + 1, 100) if sum(triplet(i, j)) == 1000]

print(res, res[0][0] * res[0][1] * res[0][2], '♥')
