# !/usr/bin/python3
# -*- coding: utf-8 -*-

import random


def triangle(n): return n * (n + 1) // 2
def square(n): return n * n
def pentagonal(n): return n * (3 * n - 1) // 2
def hexagonal(n): return n * (2 * n - 1)
def heptagonal(n): return n * (5 * n - 3) // 2
def octagonal(n): return n * (3 * n - 2)


# figurines = {'triangle': False,
#              'square': False,
#              'pentagonal': False,
#              'hexagonal': False,
#              'heptagonal': False,
#              'octagonal': False}

min_limit = 999
limit = 10_000

triangle = [triangle(n) for n in range(limit) if min_limit < triangle(n) < limit]
square = [square(n) for n in range(limit) if min_limit < square(n) < limit]
pentagonal = [pentagonal(n) for n in range(limit) if min_limit < pentagonal(n) < limit]
hexagonal = [hexagonal(n) for n in range(limit) if min_limit < hexagonal(n) < limit]
heptagonal = [heptagonal(n) for n in range(limit) if min_limit < heptagonal(n) < limit]
octagonal = [octagonal(n) for n in range(limit) if min_limit < octagonal(n) < limit]

figurines = [triangle, square, pentagonal, hexagonal, heptagonal, octagonal]

fig_bool = [False, False, False, False, False, False]

print(triangle)
print(square)
print(pentagonal)
print(hexagonal)
print(heptagonal)
print(octagonal)

print()

def find_in_all(n, ind):  #
    tmp = []
    for i, data in enumerate(figurines):
        if i != ind and not fig_bool[i]:
            for j in data:
                if str(n)[-2:] == str(j)[:2]:
                    # print(i[0], j)
                    tmp.append([i, j])
    # print('>', tmp)
    if tmp == []:
        return None
    tmp = tmp[random.randint(0, len(tmp) - 1)]
    return tmp


def find_for_6(n5, n1, ind):  #
    tmp = []
    for i, data in enumerate(figurines):
        if i != ind and not fig_bool[i]:
            for j in data:
                if str(j) == (str(n5)[-2:] + str(n1)[:2]):
                    # print(i[0], j)
                    tmp.append([i, int(str(n5)[-2:] + str(n1)[:2])])
    # print('>', tmp)
    if tmp == []:
        return None
    tmp = tmp[random.randint(0, len(tmp) - 1)]
    return tmp


arr_of_ind = []
found = False

while not found:

    for ind_arr, data_arr in enumerate(figurines):
        for n1 in data_arr:

            fig_bool = [False, False, False, False, False, False]
            arr_of_ind = []

            fig_bool[ind_arr] = True
            arr_of_ind.append(ind_arr)

            tmp = find_in_all(n1, ind_arr)
            if tmp == None:
                continue
            fig_bool[tmp[0]] = True
            arr_of_ind.append(tmp[0])
            n2 = tmp[1]

            tmp = find_in_all(n2, tmp[0])
            if tmp == None:
                continue
            fig_bool[tmp[0]] = True
            arr_of_ind.append(tmp[0])
            n3 = tmp[1]

            tmp = find_in_all(n3, tmp[0])
            if tmp == None:
                continue
            fig_bool[tmp[0]] = True
            arr_of_ind.append(tmp[0])
            n4 = tmp[1]

            tmp = find_in_all(n4, tmp[0])
            if tmp == None:
                continue
            fig_bool[tmp[0]] = True
            arr_of_ind.append(tmp[0])
            n5 = tmp[1]

            tmp = find_for_6(n5, n1, tmp[0])
            if tmp == None:
                continue
            n6 = tmp[1]
            fig_bool[tmp[0]] = True
            arr_of_ind.append(tmp[0])

            print(n1, n2, n3, n4, n5, n6)
            print(fig_bool)
            print(arr_of_ind)
            print(sum([n1, n2, n3, n4, n5, n6]), '♥')

            found = True
