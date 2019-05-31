# !/usr/bin/python3
# -*- coding: utf-8 -*-

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


