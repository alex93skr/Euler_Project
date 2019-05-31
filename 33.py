# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------33--')


arr = []


for i in range(10,100):

    if '0' not in str(i):
        arr += [i]

print(arr)


for i in arr:
    for j in arr:
        # if not i == j and str(i)[0] == str(j)[1]:
        #     # print(i, j, str(i)[0], str(j)[1])
        #     if i/j == int(str(i)[1]) / int(str(j)[0]):
        #         print(i, j)

        if not i == j and str(i)[1] == str(j)[0]:
            if i/j == int(str(i)[0]) / int(str(j)[1]):
                print(i, '/', j, '=', i/j, '-->', str(i)[0], '/', str(j)[1], '=', int(str(i)[0]) / int(str(j)[1]))



