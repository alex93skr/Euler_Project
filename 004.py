# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'-----------------------4--')

def is_palindrome(string):          # палиндром
    reversed_string = string[::-1]
    return string == reversed_string


nn = 100

for i in range(99, 1001):
    for n in range(100, 1000):
        if is_palindrome(str(i*n)):
            print(i, '*', n, '=', i*n)

