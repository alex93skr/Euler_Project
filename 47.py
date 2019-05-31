# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------47--')



def prime_factors(n):  # ДЕЛИТЕЛИ без повторов со степенями
    """Разложить число на множители"""
    # result = [1]
    factors = []
    res = []
    i = 2
    while i < n:
        if n % i == 0:
            n /= i
            factors.append(i)
        else:
            i += 1
    factors.append(int(n))

    # print(factors)

    tmparr = []
    for i in factors:
        if i not in tmparr:
            if factors.count(i) > 1:
                # tmps =
                res.append(str(i) + '**' + str(factors.count(i)))
                tmparr.append(i)
            else:
                res.append(i)
                tmparr.append(i)

    # print(res)

    return res

# prime_factors(500)


# 14 = 2 × 7
# 15 = 3 × 5

import numpy

n1=0
n2=0
n3=0
n4=0

n1_mn = 0
n2_mn = 0
n3_mn = 0
n4_mn = 0

for i in range(1_000_000):
    # print(i, len(prime_factors(i)))
    if i % 10000 == 0:
        print(i)

    if len(prime_factors(i)) == 4 and len(prime_factors(i+1)) == 4 and len(prime_factors(i+2)) == 4 and len(prime_factors(i+3)) == 4:

    # n1_mn, n2_mn, n3_mn, n4_mn = n2_mn, n3_mn, n4_mn, len(prime_factors(i))
    # if n4_mn == 4 and n3_mn == 4 and n2_mn == 4 and n1_mn == 4:

        # if not numpy.array_equal(prime_factors(i), prime_factors(i + 1)) \
        #         and not numpy.array_equal(prime_factors(i), prime_factors(i + 2)) \
        #         and not numpy.array_equal(prime_factors(i), prime_factors(i + 3)):

        print(i, prime_factors(i))
        print(i + 1, prime_factors(i + 1))
        print(i + 2, prime_factors(i + 2))
        print(i + 3, prime_factors(i + 3))
        print()



