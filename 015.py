# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------15--')

import copy

side = 3

matrix = []
routes = []


def make_matrix(n):
    for stroka in range(n):
        zz = []
        for ryad in range(n):
            zz.append('0')
        matrix.append(zz)


def print_matrix_border(name):
    for i in name:
        print(i)

def print_matrix(name):
    for i in range(side):
        for n in range(side):
            if n == side-1:
                print(name[i][n])
            else:
                print(name[i][n], ' ', end='')


step = 1

make_matrix(side)
print_matrix(matrix)
print()

for stroka in range(side):
    for ryad in range(side):
        matrix[stroka][ryad] = 'X'
        print(matrix)
        if matrix not in routes:
            routes.append(copy.deepcopy(matrix))
            step += 1
            # print_matrix(name)
            # print()
print()
# print(routes)
print(step)
print()

matrix = []

make_matrix(side)

for stroka in range(side):
    for ryad in range(side):
        matrix[ryad][stroka] = 'X'

        if matrix not in routes:
            routes.append(copy.deepcopy(matrix))
            step += 1
            print(matrix)

print()
# print(routes)
print(step)
print()

# print_matrix(routes[399])


