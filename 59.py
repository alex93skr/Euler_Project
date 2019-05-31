# !/usr/bin/python3
# -*- coding: utf-8 -*-

print('---------------------- 59 --')

#!/usr/bin/env python
# -*- coding: utf-8 -*-


with open('p059_cipher.txt') as f:
    data = f.read()


print(data)
print(type(data))
print(len(data))


arr = data.split(',')

print(arr)

for i in arr:
    print(chr(int(i)), end='')

