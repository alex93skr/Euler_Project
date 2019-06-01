# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------23--')


excess_numbers = []



def sum_divider(n):  # ДЕЛИТЕЛИ
    i = 1
    res = 0
    tmp = n / 2 + 1
    while i < tmp:
        if n % i == 0:
            res += i
        i += 1
    return res


def perfect_number(n):
    return True if n == sum_divider(n) else False



def arr_index(n):
    try:
        excess_numbers.index(n)
    except ValueError:
        return False
    else:
        return True

print(perfect_number(28))
print(arr_index(0))


ress = 0


# for i in range(28100, 11111111111):
for i in range(1, 28130):
# for i in range(1, 33):
    found = False
    for j in range(0, len(excess_numbers)):
        tmp = i - excess_numbers[j]
        # print(tmp)
        if tmp in excess_numbers:
            print(i, '(', excess_numbers[j], '+', excess_numbers[excess_numbers.index(tmp)], ')')
            found = True
            break
        else:
            pass
    if found == False:
        ress += i
        print(i, '>', ress)


print('>>', ress)


