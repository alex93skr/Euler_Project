# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------9--')

a, b, c = 1, 2, 3

for a in range(1, 1000):
    print(a)
    b = a + 1
    while b < c and b < 1000:
        b += 1
        # print(a, b, c)
        c = b + 1
        while a < b and c < 1000:
            c += 1
            # print(a, b, c)
            if (a ** 2 + b ** 2 == c ** 2) and (a + b + c == 1000):
                print('>>>', a, b, c)
                quit()

