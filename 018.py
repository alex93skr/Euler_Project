# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------18--')

tr1 = [
['', '', '', '', '', '', '', '', '', '', '', '', '', '', 75, '', '', '', '', '', '', '', '', '', '', '', '', '',''],
['', '', '', '', '', '', '', '', '', '', '', '', '', 95, '', 64, '', '', '', '', '', '', '', '', '', '', '', '',''],
['', '', '', '', '', '', '', '', '', '', '', '', 17, '', 47, '', 82, '', '', '', '', '', '', '', '', '', '', '',''],
['', '', '', '', '', '', '', '', '', '', '', 18, '', 35, '', 87, '', 10, '', '', '', '', '', '', '', '', '', '',''],
['', '', '', '', '', '', '', '', '', '', 20, '', 4, '', 82, '', 47, '', 65, '', '', '', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', '', '', 19, '', 1, '', 23, '', 75, '', 3, '', 34, '', '', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', '', 88, '', 2, '', 77, '', 73, '', 7, '', 63, '', 67, '', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', 99, '', 65, '', 4, '', 28, '', 6, '', 16, '', 70, '', 92, '', '', '', '', '', '', ''],
['', '', '', '', '', '', 41, '', 41, '', 26, '', 56, '', 83, '', 40, '', 80, '', 70, '', 33, '', '', '', '', '',''],
['', '', '', '', '', 41, '', 48, '', 72, '', 33, '', 47, '', 32, '', 37, '', 16, '', 94, '', 29, '', '', '', '',''],
['', '', '', '', 53, '', 71, '', 44, '', 65, '', 25, '', 43, '', 91, '', 52, '', 97, '', 51, '', 14, '', '', '',''],
['', '', '', 70, '', 11, '', 33, '', 28, '', 77, '', 73, '', 17, '', 78, '', 39, '', 68, '', 17, '', 57, '', '',''],
['', '', 91, '', 71, '', 52, '', 38, '', 17, '', 14, '', 91, '', 43, '', 58, '', 50, '', 27, '', 29, '', 48, '',''],
['', 63, '', 66, '', 4, '', 68, '', 89, '', 53, '', 67, '', 30, '', 73, '', 16, '', 69, '', 87, '', 40, '', 31, ''],
[4, '', 62, '', 98, '', 27, '', 23, '', 9, '', 70, '', 98, '', 73, '', 93, '', 38, '', 53, '', 60, '', 4, '', 23]]

tr = [
    ['', '', '', 3, '', '', ''],
    ['', '', 7, '', 4, '', ''],
    ['', 2, '', 4, '', 6, ''],
    [8, '', 5, '', 9, '', 3],
]

# for i in tr1:
#     print(len(i))

# print(tr[0][14])
# print(tr[1][13], tr[1][15])
# print(tr[14][28])


def print_animatrix(name):
    for i in range(len(name)):
        for j in range(len(name[i])):
            if name[i][j] == '' and j != len(name[i])-1:
                print('  ', end='')
            elif name[i][j] != '' and j != len(name[i])-1:
                print(str(name[i][j]).zfill(2), end='')
            elif name[i][j] == '' and j == len(name[i])-1:
                print('  ')
            elif name[i][j] != '' and j == len(name[i])-1:
                print(str(name[i][j]).zfill(2))


import copy
import time
import pyautogui
import sys

ttl = []
ttl_copy = []
way_max = 0

ttl_copy = copy.deepcopy(tr1)


def perebor(name, st, rd, way_n):

    global way_max

    max_st = len(name)
    max_rd = len(name[0])

    print('> RABOTAEM:', max_st, 'x', max_rd, '-', st, rd, way_n)
    # print('>>', name[st][rd], way_n)

    if way_n == '-':       # new
        ttl.append([name[st][rd]])
        way_n = 0
    else:
        ttl[way_n].append(name[st][rd])

    # print(ttl)

    if st + 1 < max_st:

        way_max += 1
        tmp = copy.deepcopy(ttl[way_n])
        ttl.append(tmp)
        tmp = str(st+1)+'x'+str(rd+1)
        ttl[way_max].append(tmp)

        # ANIMAtRiXXXXXXXXXxxxxxxxxx!!!!

        ttl_copy[st][rd] = '**'
        print_animatrix(ttl_copy)

        pyautogui.click(x=1600, y=500)
        pyautogui.hotkey('ctrl', 'l')
        # time.sleep(0.1)

        #

        perebor(name, st+1, rd-1, way_n)



# perebor(tr, 0, 3, '-')

perebor(tr1, 0, 14, '-')

print()

# for i in ttl:
#     print(i)

print('-------')

# print(len(ttl))

winner = 0

while True:
    go_next = False
    for i in range(len(ttl)):
        # print(ttl[i], len(ttl[i]))
        for j in range(len(ttl[i])):
            # print(ttl[i][j])
            # print(type(j))
            if type(ttl[i][j]) == str:
                go_next = True
                z1 = int(ttl[i][j][:ttl[i][j].find('x')])
                z2 = int(ttl[i][j][ttl[i][j].find('x')+1:])
                # print(True, z1, z2)
                del ttl[i][j]
                perebor(tr1, z1, z2, i)
    if not go_next:
        print()
        for i in ttl:
            # print(i)
            tmp = sum(i)  # 15
            if winner < tmp:
                winner = tmp
        print('>>>', winner)
        print('EXIT')

        # print(sys.getsizeof(ttl))

        quit()

