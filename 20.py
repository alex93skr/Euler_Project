# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------20--')


nn, nnn = 1, 0

for i in range(100, 0, -1):
    nn *= i

print(nn)
nn = str(nn)

for i in range(len(nn)):
    print('+', nn[i], end='')
    nnn += int(nn[i])

print('>>', nnn)


