# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------38--')

def pan_number(n):          # Пан-цифровые !!!!!!!!! без нуля
    for i in str(n):
        if i == '0':
            return False
        tmp = 0
        for j in str(n):
            # print(i , j)
            if i == j:
                tmp += 1
                if tmp > 1:
                    return False
    return True

for i in range(1, 100_000_000):
    tmp = ''
    j = 1
    while True:
        # print(tmp + str(i * j))
        if len(tmp + str(i * j)) < 11:
            tmp += str(i * j)
            # print(i, '*', j, '=', i * j, '>',tmp)
            j += 1
            if len(tmp) == 9 and pan_number(tmp):
                print('>', i, tmp)
        else:
            break
    if i % 1_000_000 == 0:
        print('>', i)


