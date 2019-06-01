# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------29--')


limits = [2,100]
res = []

for i in range(limits[0], limits[1]+1):
    for n in range(limits[0], limits[1]+1):
        tmp = i ** n
        print(i, n, tmp)
        if tmp not in res:
            res.append(tmp)

print(len(res))

