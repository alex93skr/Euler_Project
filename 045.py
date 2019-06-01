# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------45--')


t = []
p = []
h = []


def make_t(max):
    for n in range(max):
        t.append(int(n * (n + 1) / 2))


def make_p(max):
    for n in range(max):
        p.append(int(n * (3 * n - 1) / 2))

def make_h(max):
    for n in range(max):
        h.append(n * (2 * n - 1))

#                   Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Пятиугольные	 	Pn=n(3n−1)/2	1, 5, 12, 22, 35, ...
# Шестиугольные	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, .


n = 100_000

make_t(n)
make_p(n)
make_h(n)

# print(t)
# print(p)
# print(h)

# T285 = P165 = H143 = 40755.

# print(t[285])
# print(p[165])
# print(h[143])

print(len(t))
print(len(p))
print(len(h))

# for i in range(n):
#     if t[i] in p and t[i] in h:
#         print('>>', i)
#     if i % 10_000 == 0:
#         print(i)

# > 55385

print(t[55385])

