# !/usr/bin/python3
# -*- coding: utf-8 -*-

print('---------------------- 51 --')


# 000
#
# XX00
# X0X0
# X00X

# X000
# 0X00
# 00X0
# 000X


def ggo(n1, n2):       # хх  , меняея x
    for i in range(n1):
        if n2 == 0:
            print('0' * (n1), sep='')
        else:
            print('0' * i, 'X', sep='', end='')
            # if
            ggo(n1 - i - 1, n2 - 1)




ggo(4, 1)

