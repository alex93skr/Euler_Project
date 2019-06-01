# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------40--')

# 0.123456789101112131415161718192021...
#
# Видно, что 12-ая цифра дробной части - 1.

n = 1
tmp = ''

while True:
    tmp += str(n)
    # print(tmp)
    n += 1
    # if len(tmp) > 10:
    if len(tmp) > 1000100:
        print(tmp[1 - 1])
        print(tmp[10 - 1])
        print(tmp[100 - 1])
        print(tmp[1000 - 1])
        print(tmp[10000 - 1])
        print(tmp[100000 - 1])
        print(tmp[1000000 - 1])

        print(int(tmp[1 - 1]) * int(tmp[10 - 1]) * int(tmp[100 - 1]) * int(tmp[1000 - 1]) * int(tmp[10000 - 1]) * int(
            tmp[100000 - 1]) * int(tmp[1000000 - 1]))

        break

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000



