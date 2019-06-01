# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------43--')



def pan_number(n):          # Пан-цифровые
    for i in str(n):
        tmp = 0
        for j in str(n):
            # print(i , j)
            if i == j:
                tmp += 1
                if tmp > 1:
                    return False
    return True


def parts_divider(n):
    n = str(n)

    # print(n[1:4])
    # print(n[2:5])
    # print(n[3:6])
    # print(n[4:7])
    # print(n[5:8])
    # print(n[6:9])
    # print(n[7:10])

    if int(n[1:4]) % 2 ==0 \
    and int(n[2:5]) % 3 ==0 \
    and int(n[3:6]) % 5 ==0 \
    and int(n[4:7]) % 7 ==0 \
    and int(n[5:8]) % 11 ==0 \
    and int(n[6:9]) % 13 ==0 \
    and int(n[7:10]) % 17 ==0:
        return True
    else:
        return False

res = 0

from itertools import permutations      # все возможные перестановки ПЕРЕБОР
a = ('0','1','2','3','4','5','6','7','8','9')
n = 10
rep = 1
for i in permutations(a * rep, n):
    tmp = int(''.join(i))
    # print(tmp)
    if parts_divider(tmp):
        print(tmp)
        res += tmp


print('>', res)

# print(parts_divider(1406357289))
# print(parts_divider(140634589))
# print(parts_divider(1345357289))

# 1406357289

# d2d3d4=406 делится на 2 без остатка
# d3d4d5=063 делится на 3 без остатка
# d4d5d6=635 делится на 5 без остатка
# d5d6d7=357 делится на 7 без остатка
# d6d7d8=572 делится на 11 без остатка
# d7d8d9=728 делится на 13 без остатка
# d8d9d10=289 делится на 17 без остатка

