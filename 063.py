# !/usr/bin/python3
# -*- coding: utf-8 -*-

print('---------------------- 63 --')


limit = 100
res = 0

for n in range(1, limit):
    for stepen in range(limit):
        if len(str(n ** stepen)) == stepen:
            res += 1
            print(res, '>>', n, stepen, n ** stepen)



