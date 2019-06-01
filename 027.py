# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------27--')



def is_prime(n):        # простые числа		from prime
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False
    return True



# for i in range(44):
#     print(i, i**2 + i + 41, is_prime(i**2 + i + 41), (i**2 + i + 41)/41)
#
# print()
#
#
# for i in range(85):
#     print(i, i**2 - 79 * i + 1601, is_prime(i**2 - 79 * i + 1601))


lim = 1000


for a in range(-1 * lim, lim + 1):
    for b in range(-1 * lim, lim + 1):

        posled = 0
        for n in range(-1 * lim, lim + 1):
            if is_prime(n ** 2 + a * n + b):
                posled += 1
                # print(a, b, n, (n ** 2 + a * n + b), is_prime(n ** 2 + a * n + b))
            else:

                print(a,b,n,posled)
                break

# n2+an+b

