# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'-----------------------7--')


def prost(a):
    return all(a % i for i in range(2, a))


i = 1
z = 0

while True:
    i += 1
    if prost(i):
        z += 1
        print(z, i)
    if z == 10001:
        print(z, i)
        break

