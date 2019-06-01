# !/usr/bin/python3
# -*- coding: utf-8 -*-


# Треугольные	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Квадратные	 	P4,n=n2	 	        1, 4, 9, 16, 25, ...
# Пятиугольные	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Шестиугольные	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
# Семиугольные	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
# Восьмиугольные	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...

import random


def triangle(n): return n * (n + 1) // 2


def square(n): return n * n


def pentagonal(n): return n * (3 * n - 1) // 2


def hexagonal(n): return n * (2 * n - 1)


def heptagonal(n): return n * (5 * n - 3) // 2


def octagonal(n): return n * (3 * n - 2)


# 8128, 2882, 8281

# print(triangle(127))
# print(square(91))
# print(pentagonal(44))

#
# Множество является цикличным: последние две цифры каждого числа являются первыми
# двумя цифрами следующего (включая последнее и первое числа).

# Каждый тип многоугольника —
# треугольник (P3,127=8128), квадрат (P4,91=8281) и пятиугольник (P5,44=2882) —
# представлены различными числами данного множества.

# Это — единственное множество четырехзначных чисел, обладающее указанными свойствами.


figurines = {'triangle': False,
             'square': False,
             'pentagonal': False,
             'hexagonal': False,
             'heptagonal': False,
             'octagonal': False}

min_limit = 999
limit = 10_000

triangle_arr = [triangle(n) for n in range(limit) if min_limit < triangle(n) < limit]
square_arr = [square(n) for n in range(limit) if min_limit < square(n) < limit]
pentagonal_arr = [pentagonal(n) for n in range(limit) if min_limit < pentagonal(n) < limit]
hexagonal_arr = [hexagonal(n) for n in range(limit) if min_limit < hexagonal(n) < limit]
heptagonal_arr = [heptagonal(n) for n in range(limit) if min_limit < heptagonal(n) < limit]
octagonal_arr = [octagonal(n) for n in range(limit) if min_limit < octagonal(n) < limit]


# print(triangle_arr)
# print(octagonal_arr)

def fig_check(*args):
    global figurines

    print(args)

    # n = int(n)        # !!!!

    for i in args:
        if i in triangle_arr: figurines['triangle'] = True
        if i in square_arr: figurines['square'] = True
        if i in pentagonal_arr: figurines['pentagonal'] = True
        if i in hexagonal_arr: figurines['hexagonal'] = True
        if i in heptagonal_arr: figurines['heptagonal'] = True
        if i in octagonal_arr: figurines['octagonal'] = True

    # print('чек ', figurines.values())

    if all(figurines.values()):
        print('WIN')
        quit()

    figurines = {'triangle': False,
                 'square': False,
                 'pentagonal': False,
                 'hexagonal': False,
                 'heptagonal': False,
                 'octagonal': False}

    # print('ноль', figurines.values())


def gen_x(heaviness):
    if heaviness == 1:
            return str(random.randint(0, 9))  # !!!
    else:
        tmp = ''
        while heaviness != 0:
            if tmp == '':
                tmp = str(random.randint(1, 9))
            else:
                tmp += str(random.randint(0, 9))

            heaviness -= 1
    return tmp


# def gen_xxxx(prev, n_num=0):
#     global n1_start
#     if n_num == 1:
#         n1_start = gen_x(2)
#         tmp = n1_start + gen_x(2)
#     elif n_num == 6:
#         tmp = prev[-2:] + n1_start
#     else:
#         tmp = prev[-2:] + gen_x(2)
#     return tmp



# def gen_xxxx(prev, n_num=0):
#     global n1_start
#     if n_num == 1:
#         n1_start = gen_x(2)
#         tmp = n1_start + gen_x(2)
#     elif n_num == 6:
#         tmp = prev[-2:] + n1_start
#     else:
#         tmp = prev[-2:] + gen_x(2)
#     return tmp


# while True:
#     n1 = gen_xxxx(0, 1)
#     n2 = gen_xxxx(n1)
#     n3 = gen_xxxx(n2)
#     n4 = gen_xxxx(n3)
#     n5 = gen_xxxx(n4)
#     n6 = gen_xxxx(n5, 6)
#
#     fig_check(int(n1), int(n2), int(n3), int(n4), int(n5), int(n6))

    # print()


for n1_1 in range(9, 100):
    for n1_2 in range(0, 100):
        if n1_2 < 10:
            n1 = int(str(n1_1) + '0' + str(n1_2))
        else:
            n1 = int(str(n1_1) + str(n1_2))
        if len(str(n1)) != 4:
            continue

        for n2_ in range(0, 100):
            if n2_ < 10:
                n2 = int(str(n1)[-2:] + '0' + str(n2_))
            else:
                n2 = int(str(n1)[-2:] + str(n2_))
            if len(str(n2)) != 4:
                continue
            # print(n1, n2)

            for n3_ in range(0, 100):
                if n3_ < 10:
                    n3 = int(str(n2)[-2:] + '0' + str(n3_))
                else:
                    n3 = int(str(n2)[-2:] + str(n3_))
                if len(str(n3)) != 4:
                    continue
                # print(n1, n2, n3)

                for n4_ in range(0, 100):
                    if n4_ < 10:
                        n4 = int(str(n3)[-2:] + '0' + str(n4_))
                    else:
                        n4 = int(str(n3)[-2:] + str(n4_))
                    if len(str(n4)) != 4:
                        continue
                    # print(n1, n2, n3)

                    for n5_ in range(0, 100):
                        if n5_ < 10:
                            n5 = int(str(n4)[-2:] + '0' + str(n5_))
                        else:
                            n5 = int(str(n4)[-2:] + str(n5_))
                        if len(str(n5)) != 4:
                            continue
                        # print(n1, n2, n3)


                        n6 = int(str(n5)[-2:] + str(n1)[:2])
                        if len(str(n6)) != 4:
                            continue

                        # print(n1, n2, n3, n4, n5, n6)

                        fig_check(n1, n2, n3, n4, n5, n6)