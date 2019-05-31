# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------12--')

from collections import Counter


def get_ls(n):  # ДЕЛИТЕЛИ
    """Разложить число на множители"""
    # result = [1]
    result = []
    i = 2
    while i < n:
        if n % i == 0:
            n /= i
            result.append(i)
        else:
            i += 1
    result.append(int(n))
    return result


def delitel_max(zzz):
    ls = get_ls(zzz)
    kkk = dict(Counter(ls)).items()
    d = [k for k, _ in kkk]
    m = [v for _, v in kkk]
    k = [0 for _ in range(len(set(ls)))]

    ln = range(len(m))

    max = 0

    try:
        while True:
            r = 1
            for i1, i2 in zip(d, k):
                r *= i1 ** i2
            # print(r)
            max += 1

            k[0] += 1
            for i in ln:
                if k[i] > m[i]:
                    k[i] = 0
                    k[i + 1] += 1  # IndexError
    except IndexError:
        pass

    return max


for n in range(1, 10000000000):

    print('>>>', n - 1, '-e TREUG: ', end='')

    treug = 0
    for i in range(0, n):
        treug += i

    print(treug, end='')

    tmp = delitel_max(treug)

    print(' deliteley:', tmp)
    # print(n - 1, '-e teyg 4islo:', zz, 'deliteley:', delitel)

    if tmp >= 500:
        print('>>>', treug)
        quit()

