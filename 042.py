# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------42--')

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
       'W', 'X', 'Y', 'Z']


def triangular_numbers(n):
    print(int(1 / 2 * n * (n + 1)))


tri_numbers = []

for n in range(1, 1000):
    tri_numbers.append(int(1 / 2 * n * (n + 1)))

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# SKY равно 19 + 11 + 25 = 55 = t10

# print(abc.index('S')+1)
# print(abc.index('K')+1)
# print(abc.index('Y')+1)

# triangular_numbers(4)

f = open("p042_words.txt", "r")
for line in f:
    st = line
f.close()

arr = st.split(',')

print(arr)

res = 0

for i in arr:
    tmp = 0
    # print(i, '', end='')
    for j in i:
        tmp += (abc.index(j) + 1)
        # print((abc.index(j) + 1), '', end='')
    # print('>',tmp)
    if tmp in tri_numbers:
        print(i, tmp)
        res += 1

print('>>>', res)

