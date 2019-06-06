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



# Amaro Vita :coffee:
# Берем перестановки из трех символов, все возможные пароли. Расшифровываем текст. А дальше, так как он английский, в нем должны быть артикли =) С пробельчиками. Этого оказалось достаточно вполне =)



