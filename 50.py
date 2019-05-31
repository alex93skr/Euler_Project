# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------50--')



def is_prime(n):        # простые
    if n== 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False
    return True

prime = []

# max_wrk = 1_00
max_wrk = 1_000_100

for i in range(max_wrk):
    if is_prime(i):
        prime.append(i)

print(prime)

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# 953 = x + x + x +  (21 слаг)
# < 1_000_000

# print(prime.index(953))
# print(prime[12])
# print(prime[0])
print()


i = 0


super_max = 0
super_max_res = 0

for start_i in range(max_wrk):
    print()
    print('>', start_i)
    res = 0
    i = start_i

    max_start_i = 0
    max_res = 0

    while res <= max_wrk:
        if is_prime(res):
            max_res = res
            max_start_i = start_i
        # print(i, prime[i], res, is_prime(res))
        res += prime[i]
        i += 1
        # print(i, prime[i], res, is_prime(res))

    res = 0

    while res < max_res:
        print(prime[max_start_i], '', end='')

        max_start_i += 1
        res += prime[max_start_i]

    print('=', max_res, '  posled iz -', max_start_i - start_i, 'super: ', super_max, 'dlya:', super_max_res)
    if super_max < max_start_i - start_i:
        super_max = max_start_i - start_i
        super_max_res = max_res

# 41 = 2 + 3 + 5 + 7 + 11 + 13

# > 0
# 0 2 0 False
# 1 3 2 True
# 2 5 5 True
# 3 7 10 False
# 4 11 17 True
# 5 13 28 False
# 6 17 41 True
# 7 19 58 False
# 8 23 77 False
# 9 29 100 False
# 10 31 129 False

