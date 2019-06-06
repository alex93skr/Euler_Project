# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'-----------------------4--')

print(max([i * j for i in range(999, 777, -1) for j in range(999, 777, -1) if str(i * j) == str(i * j)[::-1]]), '♥')


def palindrome(string):
    """палиндром"""
    return string == string[::-1]


arr = []
for i in range(777, 1000):
    for n in range(777, 1000):
        if palindrome(str(i * n)):
            arr.append(i * n)

print('>', max(arr))
