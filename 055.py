# !/usr/bin/python3
# -*- coding: utf-8 -*-

print('---------------------- 55 --')



def if_pal(string):                    # палиндром
    return string == string[::-1]

def make_pal(string):
    return string[::-1]

def lychrel(n):
    return n + int(make_pal(str(n)))


# 47, перевернуть его и прибавить к исходному, т.е. найти 47 + 74 = 121

res = 0

# for i in range(11, 360):
# for i in range(4994 , 4994 +1 ):
for i in range(2, 10001):

    tmp = lychrel(i)
    # print('>', i, make_pal(str(i)), '=', tmp, end=' | ')

    iteration = 1

    while not if_pal(str(tmp)):


        if iteration == 100:
            print(i, iteration)
            res += 1
            break

        iteration += 1

        # print(iteration, ':', tmp, make_pal(str(tmp)), '=', lychrel(tmp), end=' | ')
        tmp = lychrel(tmp)


    # print(i, iteration)


print(res)

