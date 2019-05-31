print('---------------------- 51 --')


# 000
#
# XX00
# X0X0
# X00X

# X000
# 0X00
# 00X0
# 000X


def ggo(n1, n2):       # хх  , меняея x
    for i in range(n1):
        if n2 == 0:
            print('0' * (n1), sep='')
        else:
            print('0' * i, 'X', sep='', end='')
            # if
            ggo(n1 - i - 1, n2 - 1)




ggo(4, 1)

print('---------------------- 52 --')

# 2x, 3x, 4x, 5x и 6x


def make_arr(i, n):
    tmp = []
    for z in range(len(str(i * n))):
        tmp.append(int(str(i * n)[z]))
    print('6 :', tmp)
    return tmp


def check(i):
    check_arr = []
    for n in range(6, 0, -1):
        if n == 6:
            check_arr = make_arr(i, n)
        else:
            tmp = str(i * n)
            # print(n, tmp)

            for j in range(len(tmp)):
                print(n, i * n, '|', tmp[j], 'in', check_arr, '', end='')

                if int(tmp[j]) not in check_arr:
                    print(False)
                    return False
                print(True)
            # for j in range(len(str(i * n))):
            #     print(n, str(i * n))

            # if str(i * n)[i] not in check_arr:
            #     print(n, ':', i * n,'|', str(i * n)[i], 'in', check_arr)
            #     # print(False)
            #     return False
    return True


for i in range(1, 100000000):
    # for i in range(1, 3):
    print()
    print('>>>>', i, 2 * i, 3 * i, 4 * i, 5 * i, 6 * i)
    # check(i)
    if check(i):
        print(i, 2 * i, 3 * i,4 * i,5 * i,6 * i)
        quit()



print('---------------------- 53 --')


def arr_cut(nn):
    # print('!', nn)
    st = ''
    for i in nn:
        st += str(i)
    return st




def selection_of_items(n, arr, pref):
    # print('>>', pref)


    for i in range(len(arr)):
        print(pref, arr_cut(arr[:i]), '.', arr_cut(arr[i+1:]), sep='')

        if len(arr[i+1:]) > len(arr) - n:
            pref += arr_cut(arr[:i+1])
            # print('!', pref, '<')
            selection_of_items(n-1, arr_cut(arr[i+1:]), pref)
        else:
            print()

        # print(arr_cut(arr[:i]), '.', sep='')
        # while len(arr)



arr = [1, 2, 3, 4, 5]

print(arr_cut(arr))
print()
selection_of_items(4, arr, '')  # сколько оставить, откуда

print('---------------------- 54 --')

# Достоинство карт оценивается по порядку:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, валет, дама, король, туз.

# T - десятка, J - валет, Q - дама, K - король, A - туз;
# S - пики, C - трефы, H - червы, D - бубны.


# Старшая карта: Карта наибольшего достоинства.
# Одна пара: Две карты одного достоинства.
# Две пары: Две различные пары карт
# Тройка: Три карты одного достоинства.
# Стрейт: Все пять карт по порядку, любые масти.
# Флаш: Все пять карт одной масти.
# Фул-хаус: Три карты одного достоинства и одна пара карт.
# Каре: Четыре карты одного достоинства.
# Стрейт-флаш: Любые пять карт одной масти по порядку.
# Роял-флаш: Десятка, валет, дама, король и туз одной масти.


dignity = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']  # Достоинство
card = ['T', 'J', 'Q', 'K', 'A']  # карты
suit = ['S', 'C', 'H', 'D']  # масть


def open_case_dignity(arr):  # все значения  ['2', '3', '4', '5', '6']
    tmp = []
    for i in arr:
        tmp.append(i[0])
    return tmp


def open_case_suit(arr):  # все бложки    ['S', 'C', 'H', 'D', 'D']
    tmp = []
    for i in arr:
        tmp.append(i[1])
    return tmp


def distribute_cards(st):  # строку пополам на два массива
    return st[:14].split(' '), st[15:].split(' ')


# print(distribute_cards(test))

# ============================================================ + +

def high_card(arr):  # старшая карта
    max = -1
    arr = open_case_dignity(arr)
    for i in arr:
        if dignity.index(i) > max:
            max = dignity.index(i)
    return max


# print(high_card(['3F', '3F', 'TF', '2F', '3F']))

def comp_high_card(p1, p2):
    if high_card(p1) > high_card(p2):
        return 1
    elif high_card(p1) < high_card(p2):
        return 2


# test = '4F 2F 2F TF 2F 2F 6F 2F 2F AF'
# #
# print(comp_high_card(distribute_cards(test)[0], distribute_cards(test)[1]))


# ==================== + +

def one_pair(arr, out_res=False):  # Одна пара: Две карты одного достоинства.
    max = -1
    arr = open_case_dignity(arr)
    for i in arr:
        # print(i, arr.count(i))
        if arr.count(i) == 2:
            if dignity.index(i) > max:
                max = dignity.index(i)
    if out_res:
        return max
    return False if max == -1 else True  # индекс


# print(one_pair(['5F', 'TF', 'KF', '5F', '3F'], True))

def comp_one_pair(p1, p2):
    if one_pair(p1) and not one_pair(p2):
        return 1
    elif not one_pair(p1) and one_pair(p2):
        return 2
    elif one_pair(p1) and one_pair(p2):
        if one_pair(p1, True) > one_pair(p2, True):
            return 1
        elif one_pair(p1, True) < one_pair(p2, True):
            return 2


# test = '2F 5F 5F EF 4F 7F 4F 2F 3F TF'
# #
# print(comp_one_pair(distribute_cards(test)[0], distribute_cards(test)[1]))

# ====================  + +

def two_pairs(arr, out_res=False):  # Две пары: Две различные пары карт        по старшим парам, по младшим парам
    couples = []
    arr = open_case_dignity(arr)
    for i in arr:
        if arr.count(i) == 2:
            couples.append(dignity.index(i))
    if len(couples) != 4:
        return False
    return sorted(list(set(couples))) if out_res else True  # [0, 8]


# print(two_pairs(['3F', '5F', '3F', '5F', '1F']))
# print(two_pairs(['TF', '7F', '2F', '2F', 'TF'], True))

def comp_two_pairs(p1, p2):
    if two_pairs(p1) and not two_pairs(p2):
        return 1
    elif not two_pairs(p1) and two_pairs(p2):
        return 2
    elif two_pairs(p1) and two_pairs(p2):
        if two_pairs(p1, True)[1] > two_pairs(p2, True)[1]:
            return 1
        elif two_pairs(p1, True)[1] < two_pairs(p2, True)[1]:
            return 2
        if two_pairs(p1, True)[0] > two_pairs(p2, True)[0]:
            return 1
        elif two_pairs(p1, True)[0] < two_pairs(p2, True)[0]:
            return 2


# test = 'KF KF 2F 2F 2F 4F 4F 2F 2F TF'
# # #
# print(comp_two_pairs(distribute_cards(test)[0], distribute_cards(test)[1]))


# ====================  + +

def three(arr, out_res=False):  # Тройка: Три карты одного достоинства.     старшая
    arr = open_case_dignity(arr)
    for i in arr:
        if arr.count(i) == 3:
            return dignity.index(i) if out_res else True
    return False  # индекс


# print(three(['3F', '3F', '3F', '2F', '1F']))
# print(three(['2F', '7F', 'TF', 'TF', 'TF'], True))

def comp_three(p1, p2):
    if three(p1) and not three(p2):
        return 1
    elif not three(p1) and three(p2):
        return 2
    elif three(p1) and three(p2):
        if three(p1, True) > three(p2, True):
            return 1
        elif three(p1, True) < three(p2, True):
            return 2


# test = '4F 3F 2F 2F 4F TF 4F 2F 4F TF'
# #
# print(comp_three(distribute_cards(test)[0], distribute_cards(test)[1]))


# ==================== + + !!!!!!!!! Если Стрит составлен от Туза до Пятерки он считается самым слабым

def straight(arr, out_res=False):  # Стрейт: Все пять карт по порядку, любые масти.     старшая
    max = -1
    arr = open_case_dignity(arr)
    # print(arr)
    for i in arr:
        if dignity.index(i) > max:
            max = dignity.index(i)
    # print(max)
    # print(sorted(arr), sorted(dignity[max - 4 : max + 1]))
    if sorted(arr) != sorted(dignity[max - 4: max + 1]):
        return False
    return max if out_res else True  # индекс


# print(straight(['2F', '7F', '8F', '9F', 'TF']))
# print(straight(['2F', '3F', '4F', '5F', '6F'], True))


def comp_straight(p1, p2):
    if straight(p1) and not straight(p2):
        return 1
    elif not straight(p1) and straight(p2):
        return 2
    elif straight(p1) and straight(p2):
        if straight(p1, True) > straight(p2, True):
            return 1
        elif straight(p1, True) < straight(p2, True):
            return 2


# test = '2F 6F 4F 5F 3F 3F 4F 5F 6F 2F'
# test = '5F 6F 7F 8F 9F 3F 4F 5F 6F 2F'
# #
# print(comp_straight(distribute_cards(test)[0], distribute_cards(test)[1]))


# ====================  + +

def flush(arr, out_res=False):  # Флаш: Все пять карт одной масти.  старшая
    tmp = open_case_suit(arr)
    if tmp.count(tmp[0]) != 5:
        return False
    tmp = open_case_dignity(arr)
    max = -1
    for i in tmp:
        if dignity.index(i) > max:
            max = dignity.index(i)

    return max if out_res else True


# print(flush(['2R', '3R', '6R', '5R', '4R']))
# print(flush(['2R', '3R', '6R', '6E', '4R'], True))

def comp_flush(p1, p2):
    if flush(p1) and not flush(p2):
        return 1
    elif not flush(p1) and flush(p2):
        return 2
    elif flush(p1) and flush(p2):
        if flush(p1, True) > flush(p2, True):
            return 1
        elif flush(p1, True) < flush(p2, True):
            return 2


# test = '2F 2F 2G 2F 2F 3F 3E 5F 3F 3F'
# #
# print(comp_flush(distribute_cards(test)[0], distribute_cards(test)[1]))


# ==================== + +

def full_house(arr):  # Фул-хаус: Три карты одного достоинства и одна ПАРА карт.
    return True if three(arr) and one_pair(arr) else False


# print(full_house(['3G', '3T', 'TF', 'TR', '3F']))
# print(full_house(['2F', '2F', '2F', '2F', '3F']))


def comp_full_house(p1, p2):
    if full_house(p1) and not full_house(p2):
        return 1
    elif not full_house(p1) and full_house(p2):
        return 2
    if full_house(p1) and full_house(p2):  # по Тройкам, по Двойкам
        if three(p1, True) > three(p2, True):
            return 1
        elif three(p1, True) < three(p2, True):
            return 2
        elif one_pair(p1, True) > one_pair(p2, True):
            return 1
        elif one_pair(p1, True) < one_pair(p2, True):
            return 2


# test = '3F 4F 3F 3F 4F 2F 4F 4F 2F 2F'
#
# print(comp_full_house(distribute_cards(test)[0], distribute_cards(test)[1]))

# ====================  + +


def caret(arr, out_res=False):  # Каре: Четыре карты одного достоинства.
    arr = open_case_dignity(arr)
    for i in arr:
        # print(i, arr)
        if arr.count(i) == 4:
            return dignity.index(i) if out_res else True
    return False  # индекс


# print(caret(['TG', '3T', 'TF', 'TR', 'TF']))


def comp_caret(p1, p2):  # старшая
    if caret(p1) and not caret(p2):
        return 1
    elif not caret(p1) and caret(p2):
        return 2
    elif caret(p1) and caret(p2):
        if caret(p1, True) > caret(p2, True):
            return 1
        elif caret(p1, True) < caret(p2, True):
            return 2


# test = '4F 4F 4F EF 4F TF TF TF 3F TF'
#
# print(comp_caret(distribute_cards(test)[0], distribute_cards(test)[1]))


# ====================     + +

def straight_flush(arr, out_res=False):  # Стрейт-флаш: Любые пять карт одной масти по порядку.
    tmp = open_case_suit(arr)
    if not tmp.count(tmp[0]) == 5:
        return False
    max = -1
    arr = open_case_dignity(arr)
    # print(arr)
    for i in arr:
        tmp = dignity.index(i)
        if tmp > max:
            max = tmp
    # print(max)
    # print(sorted(arr), sorted(dignity[max - 4 : max + 1]))
    if sorted(arr) != sorted(dignity[max - 4: max + 1]):
        return False
    return max if out_res else True  # индекс


# print(straight_flush(['7E', '8E', 'JE', 'TE', '9E']))
# print(straight_flush(['7E', '8E', 'JE', 'TE', '9E'], True))


def comp_straight_flush(p1, p2):
    if straight_flush(p1) != False and straight_flush(p2) == False:
        return 1
    if straight_flush(p1) == False and straight_flush(p2) != False:
        return 2
    elif straight_flush(p1) != False and straight_flush(p2) != False:  # =
        if straight_flush(p1, True) > straight_flush(p2, True):
            return 1
        elif straight_flush(p1, True) < straight_flush(p2, True):
            return 2


# test = '2F 9F 6F 8F 7F 2F 3F 4F 5F 6F'
# #
# print(comp_straight_flush(distribute_cards(test)[0], distribute_cards(test)[1]))


# ====================  + +

def royal_flush(arr):  # Роял-флаш: Десятка, валет, дама, король и туз одной масти.
    tmp = open_case_suit(arr)
    if not tmp.count(tmp[0]) == 5:
        return False

    arr = open_case_dignity(arr)
    for i in range(8, 13):
        # print(i, dignity[i], arr)
        if dignity[i] not in arr:
            return False
    return True


def comp_royal_flush(p1, p2):
    if royal_flush(p1) and not royal_flush(p2):
        return 1
    elif not royal_flush(p1) and royal_flush(p2):
        return 2


# print(royal_flush(test))
# test = ['AF', 'KF', 'QF', 'JF', 'TF']

# ============================================================

comp_arr = [
    comp_royal_flush,
    comp_straight_flush,
    comp_caret,
    comp_full_house,
    comp_flush,
    comp_straight,
    comp_three,
    comp_two_pairs,
    comp_one_pair,
    comp_high_card]


def open_up(st):
    p1 = distribute_cards(st)[0]
    p2 = distribute_cards(st)[1]

    # print(st)
    # print(p1, p2)

    for i in comp_arr:
        tmp = i(p1, p2)
        if tmp == None:
            pass
        elif tmp == 1:
            print(st[:-1], ' >>> 1 WIN', i)
            return 1
        elif tmp == 2:
            print(st[:-1], ' >>> 2 WIN', i)
            return 2
    print(st[:-1], ' >>> DRAW !')
    return 3


# test = '8C TS KC 9H 4S TF KF QF JF AF'
# test = '4F 8F 5F 7F 6F 2C 3C 4C 5C 6C'

# print(open_up(test))
# open_up(test)

# ============================================================

ln = w1 = w2 = draw = 0

with open("p054_poker.txt") as f:  # файл по стокам
    for line in f:
        ln += 1
        tmp = open_up(line)
        if tmp == 1:
            w1 += 1
        elif tmp == 2:
            w2 += 1
        elif tmp == 3:
            draw += 1

print()
print('Все', ln, 'партий захуячены с рузельтатом:', w1, '- player 1,', w2, '- player 2,', draw, 'draw! ♥')


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

print('---------------------- 56 --')

def sum_in_string(st):
    # print(st, len(st))
    st = str(st)
    res = 0
    for i in st:
        # print(i)
        res += int(i)
    # print(res)
    return res

max = 0

for a in range(100):
    for b in range(100):
        tmp = sum_in_string(a ** b)
        if tmp > max:
            max = tmp
        print(a, b, tmp, 'win:', max)

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

print('---------------------- 58 --')



def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False
    return True




# from collections import deque

def ckeck_2prime(n):
    global prime, not_prime
    if is_prime(n):
        prime += 1
    else:
        not_prime += 1


def make_spiral_matrix(n):          # спиральная матрица ВЛЕВО
    for i in range(n):
        mat.append([0 for a in range(n)])

    row, col = n // 2, n // 2
    num = 1
    direction = 'right'

    mat[row][col] = num

    for i in range(size * size):
        num += 1
        try:
            if direction == 'right':
                col += 1
                if mat[row - 1][col] == 0:
                    direction = 'up'

            elif direction == 'up':
                row -= 1
                if mat[row][col - 1] == 0:
                    direction = 'left'

            elif direction == 'left':
                col -= 1
                if mat[row + 1][col] == 0:
                    direction = 'down'
            elif direction == 'down':
                row += 1
                if mat[row][col + 1] == 0:
                    direction = 'right'
        except IndexError:
            break
        mat[row][col] = num



def make_left_circle(n):
    global size, start_n, prime, not_prime
    max = size

    for i in range(max-1,-1,-1):
        # print(i)
        # mat[i].append(n)
        n += 1

    # tmp = []
    ckeck_2prime(n)
    n += max + 1
    for i in range(max + 2):        # take it 2
        # tmp.append(n)
        n -= 1
    # mat.insert(0, tmp)
    n += max + 3
    ckeck_2prime(n-1)

    for i in range(1, max+1):
        # print(i)
        # mat[i].insert(0, n)
        n += 1

    # tmp = []
    ckeck_2prime(n)
    for i in range(max + 2):    # take it 2
        # tmp.append(n)
        n += 1
    ckeck_2prime(n-1)
    # mat.append(tmp)

    start_n = n



mat = []
size = 3
prime = 3
not_prime = 2
# prime = 0
# not_prime = 1

make_spiral_matrix(size)


for i in mat:
    print(i)

# print()

start_n = 10

while True:
# while size != 9:
    make_left_circle(start_n)    # с какой начинать
    #
    # print()
    # for j in mat:
    #     print(j)

    print(f'size x {size+2}, prime {prime}, not prime {not_prime} ---> {round(prime/(prime + not_prime), 2)}')
    # if round(prime/(prime + not_prime), 2) < 0.11:
    #     quit()
    size += 2

    if size == 26241:
        quit()

# print()

# for i in mat:
#     print(i)

# size x 17283, prime 3630, not prime 30939 ---> 0.11
# size x 17285, prime 3630, not prime 30943 ---> 0.1

# size x 43529, prime 8271, not prime 78790 ---> 0.1
# size x 43531, prime 8271, not prime 78794 ---> 0.09

# 26233 9.997141768292684
# 26235 9.997903963414634
# 26237 9.998666158536585
# 26239 9.999428353658537
# 26241 10.000190548780488  !!!!

print('---------------------- 59 --')

#!/usr/bin/env python
# -*- coding: utf-8 -*-


with open('p059_cipher.txt') as f:
    data = f.read()


print(data)
print(type(data))
print(len(data))


arr = data.split(',')

print(arr)

for i in arr:
    print(chr(int(i)), end='')

print('---------------------- 60 --')




import eulerlib
import copy


def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False
    return True



def pr_check(n1, n2):
    return True if is_prime(int(str(n1)+str(n2))) and is_prime(int(str(n2)+str(n1))) else False

# 3, 7, 109 и 673

# print(pr_check(3, 673))



def ladder(n, max):

    prime = eulerlib.prime_numbers.primes(max)
    print(prime)
    n -= 1
    stable_values = []

    while not n == 0:

        if not stable_values == []:

            print('--- прогон, осталось', n-1)
            tmp_arr = []

            for n_x in range(len(prime)):
                for i in range(len(stable_values)):

                    if prime[n_x] in stable_values[i]:
                        # print(prime[n_x], stable_values[i], '> skip')
                        break

                    check = True
                    # print(stable_values[i])

                    for j in stable_values[i]:
                        print(prime[n_x], stable_values[i], j, '>', prime[n_x], j, '',end='')
                        if not pr_check(prime[n_x], j):
                            # print(False)
                            check = False
                            break
                        else:
                            # print(True)
                            pass

                    if check:
                        tmp = copy.deepcopy(stable_values[i])
                        tmp.append(prime[n_x])
                        tmp_arr.append(sorted(tmp))
                        # print('>', tmp_arr)

            stable_values = copy.deepcopy(tmp_arr)

        else:
            print('Перв прогон, осталось', n-1)
            for n1 in prime:
                # print(n1)
                for n2 in range(n1 + 1, len(prime)):
                    if pr_check(prime[n1], prime[n2]):
                        # print(prime[n1], prime[n2])
                        stable_values.append([prime[n1], prime[n2]])

        n -= 1

        print(stable_values, '==> SUM', sum(stable_values[0]))

ladder(5, 10000)






print('---------------------- 61 --')



print('---------------------- 62 --')



print('---------------------- 63 --')



print('---------------------- 64 --')



print('---------------------- 65 --')



print('---------------------- 66 --')



print('---------------------- 67 --')

arr = []

# with open("1.txt") as f:  # файл по стокам
with open("p067_triangle.txt") as f:  # файл по стокам
    for line in f:
        if line[-1] == '\n':
            arr.append(line[:-1])
        else:
            arr.append(line)

# print(arr)

for i in range(len(arr)):
    tmp = arr[i].split(' ')
    arr[i] = tmp

# for i in arr:
#     # print(i, len(i))
#     print(i)

print()

# нов массив РАБОЧИЙ
arrnew = []
for i in range(len(arr)):
    # tmp = round((((len(arr) - (len(arr[i]) - 1)) / 2)))-1
    tmp = len(arr) - 1 - i
    # print(len(arr), i, tmp, arr[i])

    arrtmp = []
    for j in range(int(tmp)):  # отступы слева
        arrtmp.append('')
    for j in range(len(arr[i])):  # значения
        arrtmp.append(int(arr[i][j]))
        if j != len(arr[i]) - 1:
            arrtmp.append('')
    for j in range(int(tmp)):  # отступы справа
        arrtmp.append('')
    arrnew.append(arrtmp)

# print(arrnew)

print('нов массив РАБОЧИЙ:')

for i in arrnew:
    # print(i, len(i))
    print(i)

print()

# сумма для кажд ячейки + предыдущая большая

# import copy
#
# arrsum = []

for i in range(1, len(arrnew)):
    # print(i, arrnew[i])
    for j in range(len(arrnew[i])):  #
        if arrnew[i][j] != '':
            # print(i, j, len(arrnew[i-1]), arrnew[i][j])

            if j - 1 == -1:  # нижняя слева
                # print('!!<')
                arrnew[i][j] = arrnew[i][j] + arrnew[i - 1][j + 1]
            elif j + 1 == len(arrnew[i - 1]):  # нижняя справа
                # print('!!>')
                arrnew[i][j] = arrnew[i][j] + arrnew[i - 1][j - 1]

            elif arrnew[i - 1][j - 1] == '':  # вверху слева пусто
                arrnew[i][j] = arrnew[i][j] + arrnew[i - 1][j + 1]
            elif arrnew[i - 1][j + 1] == '':  # вверху справа пусто
                arrnew[i][j] = arrnew[i][j] + arrnew[i - 1][j - 1]
            else:  # обе не пусты
                if arrnew[i][j] + arrnew[i - 1][j - 1] > arrnew[i][j] + arrnew[i - 1][j + 1]:
                    arrnew[i][j] = arrnew[i][j] + arrnew[i - 1][j - 1]
                else:
                    arrnew[i][j] = arrnew[i][j] + arrnew[i - 1][j + 1]

print('массив с сум:')
print()

for i in arrnew:
    # print(i, len(i))
    print(i)

print()

res = 0

# ответ

tmp = max(arrnew[len(arrnew) - 1][::2])  # нижняя макс
if arrnew.count(tmp) > 1:
    print('count MAX in last str > 1')
    quit()
tmp_pos = arrnew[len(arrnew) - 1].index(tmp)
print(tmp, tmp_pos)

