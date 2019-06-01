# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------19--')

day_name = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']


# 1 января 1900 года - понедельник.
# В апреле, июне, сентябре и ноябре 30 дней.
# В феврале 28 дней, в високосный год - 29.
# В остальных месяцах по 31 дню.

def month2day(n, leap_year):
    mm = 4, 6, 9, 11
    if n in mm:
        return 30
    elif n == 2 and leap_year:
        return 29
    elif n == 2 and not leap_year:
        return 28
    else:
        return 31


def leap_year(n):
    if str(n)[-2:] == '00':
        if n % 400 == 0:
            return True
        else:
            return False
    elif n % 4 == 0:
        return True
    else:
        return False


# print(leap_year(2020))
# print(month2day(12, True))

year, month, day = 1900, 1, 1
day_ow_week = 1
sunday = 0
sunday_find = 0

# year, month, day = 2000, 12, 31
# and not month == 12 and not day == 31

while True:
    leap_y = leap_year(year)
    month = 1

    while month <= 12:
        day = 1

        while day <= month2day(month, leap_y):
            print(year, leap_y, month, day, day_name[day_ow_week - 1])
            if day_ow_week == 7:
                day_ow_week = 1
                sunday += 1
                if year >= 1901 and day == 1:
                    sunday_find += 1
            else:
                day_ow_week += 1
            if year == 2000 and month == 12 and day == 31:
                print()
                print('Всего воскресений:', sunday)
                print('Воскресений на первое число месяца:', sunday_find)
                quit()
            day += 1
        month += 1
    year += 1

# с 1 января 1901 года до 31 декабря 2000 года)?

# 1	Январь
# 2	Февраль
# 3	Март
# 4	Апрель
# 5	Май
# 6	Июнь
# 7	Июль
# 8	Август
# 9	Сентябрь
# 10	Октябрь
# 11	Ноябрь
# 12	Декабрь


# Високосный год - любой год, делящийся нацело на 4,
# однако последний год века (ХХ00) является високосным в том и только том случае,
# если делится на 400.



