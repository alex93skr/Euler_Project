# !/usr/bin/python3
# -*- coding: utf-8 -*-

print(f'-----------------------5--')

def euler5(limit):
  hasNumberFound = False
  iterator = 1

  while not hasNumberFound:
    num = limit * iterator

    for divider in range(2, limit):
      if num % divider != 0:
        break
    else:
      hasNumberFound = True
      return num
    iterator += 1

print( euler5(20) )

