# !/usr/bin/python3
# -*- coding: utf-8 -*-

print('---------------------- 62 --')


def comp(n1, n2):
    return True if sorted([*str(n1)]) == sorted([*str(n2)]) else False


print(comp(123123, 123123))


# 41063625 (345)
# 56623104 (384)
# 66430125 (405)

limit = 100000

for n1 in range(limit):
    print(n1)

    for n2 in range(n1, limit):
        if n1 == n2: continue
        if comp(n1 ** 3, n2 ** 3):

            for n3 in range(n2, limit):
                if n1 == n3 or n2 == n3: continue
                if comp(n1 ** 3, n3 ** 3):

                    # print(n1, n2, n3, '>', n1 ** 3, n2 ** 3, n3 ** 3)

                    for n4 in range(n3, limit):
                        if n1 == n4 or n2 == n4 or n3 == n4: continue
                        if comp(n1 ** 3, n4 ** 3):

                            for n5 in range(n4, limit):
                                if n1 == n5 or n2 == n5 or n3 == n5 or n4 == n5: continue
                                if comp(n1 ** 3, n5 ** 3):

                                    for n6 in range(n5, limit):
                                        if n1 == n6 or n2 == n6 or n3 == n6 or n4 == n6 or n5 == n6: continue
                                        if comp(n1 ** 3, n6 ** 3):


                                            print(n1, n2, n3,  n4, n5, n6, '>', n1 ** 3, n2 ** 3, n3 ** 3)
                                            quit()
