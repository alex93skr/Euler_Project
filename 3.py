# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'-----------------------3--')



n = 600851475143
i = 2
while i * i <= n:
    while n % i == 0:
        n = n / i
    i = i + 1
print(n)

# def prost(a):
#     return all(a % i for i in range(2, int(a)))


# print(prost(3))
# print(prost(4))

#
# i = 2
# while True:
#     if i < 60085147514 and 600851475143 % i == 0:
#         print('600851475143 /', i, '=', 600851475143 / i, prost(600851475143 / i))
#     i += 1


