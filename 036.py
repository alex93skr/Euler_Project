# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------36--')

def palindrome(string):                    # палиндром
    reversed_string = string[::-1]
    return string == reversed_string

res = 0

for i in range(1, 1_000_001):
    # print(i, palindrome(str(i)), bin(i), str(bin(i))[2:])
    if palindrome(str(i)) and str(bin(i))[2] != 0 and palindrome(str(bin(i))[2:]):
        print(i, str(bin(i))[2:], True)
        res += i

print('>', res)

