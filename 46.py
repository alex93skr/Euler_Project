# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------46--')


def is_prime(n):        # простые
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False
    return True


print()


double_square = []

for i in range(1, 100000):
    # print(i, 2 * (i ** 2))
    double_square.append(2 * (i ** 2))
# 99 > 19602


# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12


def goldbach(n):
    for i in range(n):
        if is_prime(n - double_square[i]):
            return True
    return False


print()

for i in range(3, 10000000, 2):   # нечетное составное
    if not is_prime(i):
        print(i)
        if not goldbach(i):
            print('>>', i)
            quit()



