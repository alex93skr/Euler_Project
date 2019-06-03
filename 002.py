# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'-----------------------2--')

sum = 2

fb1 = 1
fb2 = 2
i = 3
nn1, nn2 = 0, 0

while i <= 4_000_000:
    # print(i, end='')
    if i % 2 == 0:
        # print(' shet')
        sum += i
    fb1 = fb2
    fb2 = i
    i = fb1 + fb2

print('>>>', sum, '♥')


