# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------44--')

max_step = 10000

pen = []

for i in range(1, max_step):
    # print( int(i * (3 * i - 1) / 2) )
    pen.append(int(i * (3 * i - 1) / 2))

print(pen)

# pen = dict(pen)
# print(pen)

# n(3n−1)/2
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...


# P4 + P7 = 22 + 70 = 92 = P8

res = []

for i in range(int(max_step / 2)):
    print(i)
    for j in range(i):

        # print(i, j, '|', pen[i], pen[j])

        # if pen[i] + pen[j] in pen:
        #     print(i, j, '---',

        # res.append([pen[i], '-', pen[j], '=',
        #             pen[i] - pen[j])

        if pen[i] + pen[j] in pen and pen[i] - pen[j] in pen:
            print(i, j, '---', pen[i], pen[j])
            res.append([pen[i], pen[j]])

print(res)

# 2166 1019 --- 7042750 1560090

