# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------35--')

def is_prime(n):        # простые
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False
    return True

# print(is_prime(5))

def permutation(n):
    n = str(n)
    for i in range(len(n)-1):
        n = n[1:] + n[0]
        print(n, '',end='')
        if not is_prime(int(n)):
            return False
    return True


permutation(10)

res = 0

for i in range(1_000_001):
# for i in range(1000):
    if is_prime(i):
        print(i, ': ', end='')
        if permutation(i):
            res += 1
        print()


# 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97

print('>', res)

