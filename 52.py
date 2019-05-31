# !/usr/bin/python3
# -*- coding: utf-8 -*-

print('---------------------- 52 --')

# 2x, 3x, 4x, 5x и 6x


def make_arr(i, n):
    tmp = []
    for z in range(len(str(i * n))):
        tmp.append(int(str(i * n)[z]))
    print('6 :', tmp)
    return tmp


def check(i):
    check_arr = []
    for n in range(6, 0, -1):
        if n == 6:
            check_arr = make_arr(i, n)
        else:
            tmp = str(i * n)
            # print(n, tmp)

            for j in range(len(tmp)):
                print(n, i * n, '|', tmp[j], 'in', check_arr, '', end='')

                if int(tmp[j]) not in check_arr:
                    print(False)
                    return False
                print(True)
            # for j in range(len(str(i * n))):
            #     print(n, str(i * n))

            # if str(i * n)[i] not in check_arr:
            #     print(n, ':', i * n,'|', str(i * n)[i], 'in', check_arr)
            #     # print(False)
            #     return False
    return True


for i in range(1, 100000000):
    # for i in range(1, 3):
    print()
    print('>>>>', i, 2 * i, 3 * i, 4 * i, 5 * i, 6 * i)
    # check(i)
    if check(i):
        print(i, 2 * i, 3 * i,4 * i,5 * i,6 * i)
        quit()



