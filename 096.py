# !/usr/bin/python3
# -*- coding: utf-8 -*-

print('---------------------- 96 --')
import random
from copy import deepcopy


def load_file():
    data = []
    tmp = []
    n = 0
    with open("p096_sudoku.txt") as f:
        for line in f:
            # print(n, line[:-1])
            if n == 0:
                n += 1
            else:
                tmp.append([int(i) for i in line[:-1]])
                n += 1
            if n == 10:
                data.append(tmp)
                tmp = []
                n = 0
    # print(data)
    # print(len(data))
    # for i in data:
    #     print(len(i))
    #
    return data


def ves_riad(arr, col):
    tmp = []
    for i in arr:
        tmp.append(i[col])
    # print(tmp)
    return tmp


def nice_print(arr):
    for st_n, st in enumerate(arr):
        for rd_n, rd in enumerate(st):
            print(rd, ' ', end='')
            if rd_n == 2 or rd_n == 5:
                print(' ', end='')
        print()
        if st_n == 2 or st_n == 5:
            print()
    print('-------------------')


def sud_win(arr):
    for st_n, st in enumerate(arr):
        for rd_n, rd in enumerate(st):
            if rd != 0 and st.count(rd) == 1 and ves_riad(arr, rd_n).count(rd) == 1:
                pass
            else:
                return False
    return True


# win = [[4, 8, 3, 9, 2, 1, 6, 5, 7], [9, 6, 7, 3, 4, 5, 8, 2, 1], [2, 5, 1, 8, 7, 6, 4, 9, 3], [5, 4, 8, 1, 3, 2, 9, 7, 6], [7, 2, 9, 5, 6, 4, 1, 3, 8], [1, 3, 6, 7, 9, 8, 2, 4, 5], [3, 7, 2, 6, 8, 9, 5, 1, 4], [8, 1, 4, 2, 5, 3, 7, 6, 9], [6, 9, 5, 4, 1, 7, 3, 8, 2]]
# nice_print(win)
# print(sud_win(win))


# tst = ['003020600', '900305001', '001806400', '008102900', '700000008', '006708200', '002609500', '800203009', '005010300']

tst0 = [[0, 0, 3, 0, 2, 0, 6, 0, 0], [9, 0, 0, 3, 0, 5, 0, 0, 1], [0, 0, 1, 8, 0, 6, 4, 0, 0],
        [0, 0, 8, 1, 0, 2, 9, 0, 0], [7, 0, 0, 0, 0, 0, 0, 0, 8], [0, 0, 6, 7, 0, 8, 2, 0, 0],
        [0, 0, 2, 6, 0, 9, 5, 0, 0], [8, 0, 0, 2, 0, 3, 0, 0, 9], [0, 0, 5, 0, 1, 0, 3, 0, 0]]


# nice_print(tst0)
# print()
# ves_riad(tst, 8)

# 0  0  3   0  2  0   6  0  0
# 9  0  0   3  0  5   0  0  1
# 0  0  1   8  0  6   4  0  0
#
# 0  0  8   1  0  2   9  0  0
# 7  0  0   0  0  0   0  0  8
# 0  0  6   7  0  8   2  0  0
#
# 0  0  2   6  0  9   5  0  0
# 8  0  0   2  0  3   0  0  9
# 0  0  5   0  1  0   3  0  0


def minikvadrat(arr, st_n, rd_n):
    # print(st_n, rd_n)

    tmp = []

    if st_n < 3: st = [0, 1, 2]
    if 2 < st_n < 6: st = [3, 4, 5]
    if 5 < st_n: st = [6, 7, 8]

    if rd_n < 3: rd = [0, 1, 2]
    if 2 < rd_n < 6: rd = [3, 4, 5]
    if 5 < rd_n: rd = [6, 7, 8]
    # print(st, rd)

    for i in st:
        for j in rd:
            # print(arr[i][j])
            tmp.append(arr[i][j])
    return tmp


def rend_arr():
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(a)):
        tmp = random.randint(1, 9)
        while tmp in a:
            tmp = random.randint(1, 9)
        a[i] = tmp
    # a = [random.randint(1, 10)]
    # print(a)
    return a


def fnd_obvious_singles(arr):
    n = 0
    for st_n, st in enumerate(arr):
        for rd_n, rd in enumerate(st):
            if rd == 0:
                tmp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for i in range(1, 10):
                    if (i in st) or (i in ves_riad(arr, rd_n)) or (i in minikvadrat(arr, st_n, rd_n)):
                        # print(rd, '>', st_n, rd_n, '>>', i, tmp)
                        del tmp[tmp.index(i)]
                    # print()
                # print('            ', tmp)
                if len(tmp) == 1:
                    arr[st_n][rd_n] = tmp[0]
                    n += 1
                # else:
                #     arr[st_n][rd_n] = tmp
            # else:
            # print(rd, '>')
    print('fnd obvious singles -', n)
    # nice_print(arr)
    if n != 0:
        return True
    else:
        return False


# ===============


def fnd_obvious_singles_witharr(arr):
    n = 0
    for st_n, st in enumerate(arr):
        for rd_n, rd in enumerate(st):
            if rd == 0:
                tmp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for i in range(1, 10):
                    if (i in st) or (i in ves_riad(arr, rd_n)) or (i in minikvadrat(arr, st_n, rd_n)):
                        # print(rd, '>', st_n, rd_n, '>>', i, tmp)
                        del tmp[tmp.index(i)]
                    # print()
                # print('            ', tmp)
                if len(tmp) == 1:
                    arr[st_n][rd_n] = tmp[0]
                    n += 1
                else:
                    arr[st_n][rd_n] = tmp
            # else:
            # print(rd, '>')
    print('fnd obvious with arr -', n)
    # nice_print(arr)
    # if n != 0:
    #     return True
    # else:
    #     return False


# ===============


def perebor(arr, nn):
    n_iter = 0
    tst = deepcopy(arr)
    while not sud_win(tst):
        n_iter += 1
        if n_iter % 5_000 == 0:
            print(nn, n_iter)
        next = True
        # print(False)
        tst = deepcopy(arr)
        for st_n, st in enumerate(tst):
            if next == False:
                break
            for rd_n, rd in enumerate(st):
                if next == False:
                    break
                if rd == 0:
                    tmp = rend_arr()
                    for i in tmp:
                        # print(i, minikvadrat(tst, st_n, rd_n))
                        if (i in st) or (i in ves_riad(tst, rd_n)) or (i in minikvadrat(tst, st_n, rd_n)):
                            pass
                        else:
                            # print(rd_n*'   ', i)
                            tst[st_n][rd_n] = i
                            break
                    if tst[st_n][rd_n] == 0:
                        # print('False')
                        next = False

    # nice_print(tst)
    print(tst)
    return tst


# =====================


def rend_win(arr):
    pomena = 0
    # found = True
    for st_n, st in enumerate(arr):
        # if not found: break
        for rd_n, rd in enumerate(st):
            # if not found: break
            if type(rd) == list:
                len_n = len(arr[st_n][rd_n]) - 1
                rndind = random.randint(0, len_n)
                i = arr[st_n][rd_n][rndind]

                if (i not in st) and (i not in ves_riad(arr, rd_n)) and (i not in minikvadrat(arr, st_n, rd_n)):
                    arr[st_n][rd_n] = arr[st_n][rd_n][rndind]
                    pomena += 1
                else:
                    # found = False
                    # print(False)
                    # print('pomena', pomena)
                    return
                # print(st_n, rd_n, 'LIST', rd, '>', len_n, rndind, '>>', arr[st_n][rd_n])


# =====================

def recursive_selection(arr, st_start, rd_start):
    # nice_print(arr)
    print('rec..')
    for st_n in range(st_start, len(arr)):
        for rd_n in range(rd_start, len(arr)):
            if type(arr[st_n][rd_n]) == list:
                for i in arr[st_n][rd_n]:
                    # print(arr[st_n][rd_n], i, arr[st_n], ves_riad(arr, rd_n), minikvadrat(arr, st_n, rd_n))
                    if (i not in arr[st_n]) and (i not in ves_riad(arr, rd_n)) and (i not in minikvadrat(arr, st_n, rd_n)):

                        print(arr[st_n][rd_n], i)

                        arr[st_n][rd_n] = i

                        if st_n+1 != 9 and rd_n+1 != 9:
                            print('>')
                            recursive_selection(deepcopy(arr), st_n, rd_n + 1)
                        elif st_n+1 != 9 and rd_n+1 == 9:
                            print('>>')

                            recursive_selection(deepcopy(arr), st_n + 1, 0)
                        elif st_n + 1 == 9 and rd_n + 1 != 9:
                            print('>>>')

                            recursive_selection(deepcopy(arr), 8, rd_n + 1)
                    else:
                        break
                        # nice_print(arr)
    # nice_print(arr)
                        # if st_n+1 == 9 and rd_n+1 == 9:
                        #     nice_print(arr)
                        #     break
                        # else:
                        #     # nice_print(arr)
                        #     recursive_selection(arr, st_n+1, rd_n+1)




# ====================

def startgame(arr):
    # nice_print(arr)

    while fnd_obvious_singles(arr):
        pass

    if sud_win(arr):
        print('WIN')
        return arr
    else:
        print('perebor ...')
        fnd_obvious_singles_witharr(arr)
        nice_print(arr)
        wrk = deepcopy(arr)
        recursive_selection(wrk, 0, 0)

    return arr

    # fnd_obvious_singles_witharr(arr)
    # nice_print(arr)

    # n = 0
    # wrk = deepcopy(arr)
    # rend_win(wrk)
    # n += 1
    #
    # nice_print(wrk)
    #
    # while not sud_win(wrk):
    #     wrk = deepcopy(arr)
    #     rend_win(wrk)
    #     n += 1
    #     print('perebor', n)
    # quit()

    # nice_print(arr)

    # wrk = deepcopy(arr)
    # rend_win(wrk)
    #
    # nice_print(wrk)
    #
    # while not sud_win(wrk):
    #     wrk = deepcopy(arr)
    #     rend_win(wrk)


# startgame(tst0)

# nice_print(tst0)


data = load_file()
print(len(data))

n = 0
win_arr = []

startgame(data[1])

# for i in data:
#     n += 1
#     print()
#     print(n, i)
#     win_arr.append(startgame(i))
#     print(win_arr)
