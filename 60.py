# !/usr/bin/python3
# -*- coding: utf-8 -*-

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






