# !/usr/bin/python3
# -*- coding: utf-8 -*-

print('---------------------- 57 --')

# √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
#
#
# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
#
#
# Следующие три приближения: 99/70, 239/169 и 577/408, а восьмое приближение, 1393/985


n = 0

# form = 1 + 1/(2 + n)

# print(form)
form = '1 + (1 / (2 + n))'
znam = '(2 + n)'

for i in range(0, 5):
    form_str = 'print(' + form + ', end="")'
    znam_str = 'print(' + znam + ', end="")'

    print('>', znam_str, ' |  XX / ', end='')
    eval(znam_str)
    print(' = ', end='')
    eval(form_str)

    print()

    n_st = '1/(2 + n)'
    znam = znam[:znam.find('n')] + n_st + znam[znam.find('n') + 1:]
    form = form[:form.find('n')] + n_st + form[form.find('n') + 1:]
    # print(':      ', form)

