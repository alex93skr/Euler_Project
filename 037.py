# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------37--')



def is_prime(n):        # простые
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False
    return True

# 3797
# 3797, 797, 97, 7
# 3797, 379, 37, 3


def remove_left(n):
    n = str(n)
    for i in range(len(n)-1):
        n = n[1:]
        # print(n)
        if not is_prime(int(n)):
            return False
    return True

def remove_right(n):
    n = str(n)
    for i in range(len(n)-1):
        n = n[:-1]
        # print(n)
        if not is_prime(int(n)):
            return False
    return True


res = 0

for i in range(10, 100000000):
    if is_prime(i) and remove_left(i) and remove_right(i):
        res += i
        print(i, res)
    if i % 100_000 == 0:
        print('>', i)


