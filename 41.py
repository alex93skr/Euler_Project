# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------41--')

def is_prime(n):        # простые
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False
    return True

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


from itertools import permutations      # все возможные перестановки ПЕРЕБОР
a = ('7','6','5','4','3','2','1')
n = 7
rep = 1
for i in permutations(a * rep, n):
    tmp = int(''.join(i))
    # print(tmp)
    if is_prime(tmp) and pan_number(tmp):
        print(tmp)

