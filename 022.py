# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------22--')

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
       'W', 'X', 'Y', 'Z']
st = ''


def letter_number(n):
    return abc.index(n) + 1

f = open("names.txt", "r")
for line in f:
    st = line
f.close()

arr = st.split(',')
arr.sort()
res = 0

for i in range(len(arr)):
    print(i + 1, arr[i], '> ', end='')
    sum_i = 0
    for n in arr[i]:
        tmp = letter_number(n)
        print(tmp, ' ', sep='', end='')
        sum_i += int(tmp)
    points = (i + 1) * sum_i
    res += points

    print('=', sum_i, points, res)


