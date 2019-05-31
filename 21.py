# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------21--')


def divider(n):     # ДЕЛИТЕЛИ
    result = []
    i = 1
    while i < n:
        if n % i == 0:
            result.append(i)
        i += 1
    return result

arr = []
res = 0

for i in range(10001):
    tmp = sum(divider(i))
    print(i, tmp)
    arr.append([i, tmp])

print()

for i in range(len(arr)):

    for j in range(len(arr)):
        if not arr[i][0] == arr[i][1] and arr[i][0] == arr[j][1] and arr[i][1] == arr[j][0]:
            print(arr[i], arr[j])
            res += arr[i][0] + arr[j][1]

print('>>', res, '/ 2 =', int(res/2))


