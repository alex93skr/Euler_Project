# !/usr/bin/python3
# -*- coding: utf-8 -*-

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

