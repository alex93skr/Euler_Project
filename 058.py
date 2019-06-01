# !/usr/bin/python3
# -*- coding: utf-8 -*-

print('---------------------- 58 --')



def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False
    return True




# from collections import deque

def ckeck_2prime(n):
    global prime, not_prime
    if is_prime(n):
        prime += 1
    else:
        not_prime += 1


def make_spiral_matrix(n):          # спиральная матрица ВЛЕВО
    for i in range(n):
        mat.append([0 for a in range(n)])

    row, col = n // 2, n // 2
    num = 1
    direction = 'right'

    mat[row][col] = num

    for i in range(size * size):
        num += 1
        try:
            if direction == 'right':
                col += 1
                if mat[row - 1][col] == 0:
                    direction = 'up'

            elif direction == 'up':
                row -= 1
                if mat[row][col - 1] == 0:
                    direction = 'left'

            elif direction == 'left':
                col -= 1
                if mat[row + 1][col] == 0:
                    direction = 'down'
            elif direction == 'down':
                row += 1
                if mat[row][col + 1] == 0:
                    direction = 'right'
        except IndexError:
            break
        mat[row][col] = num



def make_left_circle(n):
    global size, start_n, prime, not_prime
    max = size

    for i in range(max-1,-1,-1):
        # print(i)
        # mat[i].append(n)
        n += 1

    # tmp = []
    ckeck_2prime(n)
    n += max + 1
    for i in range(max + 2):        # take it 2
        # tmp.append(n)
        n -= 1
    # mat.insert(0, tmp)
    n += max + 3
    ckeck_2prime(n-1)

    for i in range(1, max+1):
        # print(i)
        # mat[i].insert(0, n)
        n += 1

    # tmp = []
    ckeck_2prime(n)
    for i in range(max + 2):    # take it 2
        # tmp.append(n)
        n += 1
    ckeck_2prime(n-1)
    # mat.append(tmp)

    start_n = n



mat = []
size = 3
prime = 3
not_prime = 2
# prime = 0
# not_prime = 1

make_spiral_matrix(size)


for i in mat:
    print(i)

# print()

start_n = 10

while True:
# while size != 9:
    make_left_circle(start_n)    # с какой начинать
    #
    # print()
    # for j in mat:
    #     print(j)

    print(f'size x {size+2}, prime {prime}, not prime {not_prime} ---> {round(prime/(prime + not_prime), 2)}')
    # if round(prime/(prime + not_prime), 2) < 0.11:
    #     quit()
    size += 2

    if size == 26241:
        quit()

# print()

# for i in mat:
#     print(i)

# size x 17283, prime 3630, not prime 30939 ---> 0.11
# size x 17285, prime 3630, not prime 30943 ---> 0.1

# size x 43529, prime 8271, not prime 78790 ---> 0.1
# size x 43531, prime 8271, not prime 78794 ---> 0.09

# 26233 9.997141768292684
# 26235 9.997903963414634
# 26237 9.998666158536585
# 26239 9.999428353658537
# 26241 10.000190548780488  !!!!

