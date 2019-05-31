# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'-----------------------6--')

# # (1 + 2 + ... + 10)2 = 552 = 3025
zz1 = 0
for i in range(1, 101):
    zz1 += i
    # print(i, zz1)
print('>>', zz1 ** 2)

# 12 + 22 + ... + 102 = 385
zz2 = 0
for ttt in range(1, 101):
    zz2 += ttt ** 2
    # print(ttt, zz2)
print('>>', zz2)

# # 3025 − 385 = 2640.

zz3 = zz1 ** 2 - zz2

print(zz1 ** 2, zz2, zz3)
