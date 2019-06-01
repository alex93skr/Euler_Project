# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------28--')


# 5 на 5
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# ряды - rows
# столбы - columns


mat = []


def make_spiral_matrix(n):      # спиральная матрица ВПРАВО
    for i in range(n):
        mat.append([0 for a in range(n)])

    row, col = n // 2, n // 2
    num = 1
    direction = 'right'

    mat[row][col] = num

    # for i in mat:
    #     print(i)

    print()

    while True:

        num += 1
        # print(num, '>', row, col, direction)

        try:
            if direction == 'right':
                col += 1
                if mat[row + 1][col] == 0:
                    direction = 'down'
            elif direction == 'down':
                row += 1
                if mat[row][col - 1] == 0:
                    direction = 'left'
            elif direction == 'left':
                col -= 1
                if mat[row - 1][col] == 0:
                    direction = 'up'
            elif direction == 'up':
                row -= 1
                if mat[row][col + 1] == 0:
                    direction = 'right'
        except IndexError:
            break

        # print(num, '>>', row, col, direction)

        mat[row][col] = num

        # for i in mat:
        #     print(i)
        #
        # print()

def sum_diagonals(name):
    res = 0
    for i in range(len(name)):
        print('>', res, name[i][i])
        res = res + name[i][i]
    print()
    n = 0
    for i in range(len(name)-1, -1, -1):
        print('>>', res, i, n, name[i][n])
        res = res + name[i][n]
        n += 1

    print(res)
    res = res - name[len(name) // 2][len(name) // 2]
    print(res)


make_spiral_matrix(1001)


print()

for i in mat:
    print(i)

print()


sum_diagonals(mat)


