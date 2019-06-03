# !/usr/bin/python3
# -*- coding: utf-8 -*-
import time

print(f'-----------------------4--')


def euler5(limit):

    found = False
    z = 1
    n = limit

    while not found:
        # print(n)

        found = True
        for i in range(2, limit+1):
            if not n % i == 0:
                found = False
                break
        z += 1
        n = limit * z

        # if any(n % i != 0 for i in range(2, limit+1)):
        #     z += 1
        #     n = limit * z
        # else:
        #     return n

    return n

t1 = time.perf_counter_ns()

print(euler5(20), (time.perf_counter_ns() - t1)/1000000000)




# def euler5(limit):
#
#     limit += 1
#     iterator = 1
#
#     while True:
#         num = limit * iterator
#
#         for divider in range(2, limit):
#             if num % divider != 0:
#                 break
#         else:
#             return num
#
#         iterator += 1




