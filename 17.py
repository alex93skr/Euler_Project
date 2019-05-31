# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'----------------------17--')


units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
         "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
scales = ["hundred", "thousand", "million", "billion", "trillion"]


def int2text(num):
    st = ''

    if str(num)[-4:-3]:
        st += units[int(str(num)[-4:-3])] + scales[1]
        # print('>', units[int(str(num)[-4:-3])], scales[1])
        if str(num)[-3:] == '000':
            return st
    if str(num)[-3:-2]:
        st += units[int(str(num)[-3:-2])] + scales[0]
        # print('>', units[int(str(num)[-3:-2])], scales[0])
        if str(num)[-2:] == '00':
            return st

        # print('> and')
        st += 'and'

    if str(num)[-2:-1]:  # двузнач
        if int(str(num)[-2:]) > 19:
            st += tens[int(str(num)[-2:-1])]
            # print('>', tens[int(str(num)[-2:-1])])
            if not int(str(num)[-1]) == 0:  # ноль вконце
                st += units[int(str(num)[-1])]
                # print('>', units[int(str(num)[-1])])
        else:
            st += units[int(str(num)[-2:])]
            # print('>', units[int(str(num)[-2:])])

    else:  # одознач
        st += units[int(str(num)[-1])]
        # print('>', units[int(str(num)[-1])])
    return st


def count_characters(st):
    # print(len(st.replace('-', '').replace(' ', '')))
    return len(st.replace('-', '').replace(' ', ''))


nn = 0

for i in range(1, 1001):
    nn += count_characters(int2text(i))
    print(i, int2text(i), count_characters(int2text(i)), nn)


