# !/usr/bin/python3
# -*- coding: utf-8 -*-

print('---------------------- 67 --')

arr = []

# with open("1.txt") as f:  # файл по стокам
with open("p067_triangle.txt") as f:  # файл по стокам
    for line in f:
        if line[-1] == '\n':
            arr.append(line[:-1])
        else:
            arr.append(line)

# print(arr)

for i in range(len(arr)):
    tmp = arr[i].split(' ')
    arr[i] = tmp

# for i in arr:
#     # print(i, len(i))
#     print(i)

print()

# нов массив РАБОЧИЙ
arrnew = []
for i in range(len(arr)):
    # tmp = round((((len(arr) - (len(arr[i]) - 1)) / 2)))-1
    tmp = len(arr) - 1 - i
    # print(len(arr), i, tmp, arr[i])

    arrtmp = []
    for j in range(int(tmp)):  # отступы слева
        arrtmp.append('')
    for j in range(len(arr[i])):  # значения
        arrtmp.append(int(arr[i][j]))
        if j != len(arr[i]) - 1:
            arrtmp.append('')
    for j in range(int(tmp)):  # отступы справа
        arrtmp.append('')
    arrnew.append(arrtmp)

# print(arrnew)

print('нов массив РАБОЧИЙ:')

for i in arrnew:
    # print(i, len(i))
    print(i)

print()

# сумма для кажд ячейки + предыдущая большая

# import copy
#
# arrsum = []

for i in range(1, len(arrnew)):
    # print(i, arrnew[i])
    for j in range(len(arrnew[i])):  #
        if arrnew[i][j] != '':
            # print(i, j, len(arrnew[i-1]), arrnew[i][j])

            if j - 1 == -1:  # нижняя слева
                # print('!!<')
                arrnew[i][j] = arrnew[i][j] + arrnew[i - 1][j + 1]
            elif j + 1 == len(arrnew[i - 1]):  # нижняя справа
                # print('!!>')
                arrnew[i][j] = arrnew[i][j] + arrnew[i - 1][j - 1]

            elif arrnew[i - 1][j - 1] == '':  # вверху слева пусто
                arrnew[i][j] = arrnew[i][j] + arrnew[i - 1][j + 1]
            elif arrnew[i - 1][j + 1] == '':  # вверху справа пусто
                arrnew[i][j] = arrnew[i][j] + arrnew[i - 1][j - 1]
            else:  # обе не пусты
                if arrnew[i][j] + arrnew[i - 1][j - 1] > arrnew[i][j] + arrnew[i - 1][j + 1]:
                    arrnew[i][j] = arrnew[i][j] + arrnew[i - 1][j - 1]
                else:
                    arrnew[i][j] = arrnew[i][j] + arrnew[i - 1][j + 1]

print('массив с сум:')
print()

for i in arrnew:
    # print(i, len(i))
    print(i)

print()

res = 0

# ответ

tmp = max(arrnew[len(arrnew) - 1][::2])  # нижняя макс
if arrnew.count(tmp) > 1:
    print('count MAX in last str > 1')
    quit()
tmp_pos = arrnew[len(arrnew) - 1].index(tmp)
print(tmp, tmp_pos)

