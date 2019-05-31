# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------14--')

elem = 0
shag_max = 0

for i in range(1, 1_000_000):
    shag = i
    shag_n = 1

    # print(shag, '-> ', end='')

    while shag > 1:
        if shag % 2 == 0:  # чет
            shag //= 2
            # print(shag, ' ', end='')
        else:
            shag = 3 * shag + 1
            # print(shag, ' ', end='')
        shag_n += 1

    # print(shag)
    # print('SHAGOV -', shag_n)
    if shag_n > shag_max:
        elem = i
        shag_max = shag_n

print('>>>', elem, shag_max)

