


import sys


# def get_block():

def getnumber(st):
    tmp = ''
    for i in range(15, len(st)-4):
        if st[i] != '-' and st[i] != ' ':
            tmp += str(st[i])
    print('>', tmp)
    return tmp


data = []

with open('_euler51-.py', 'r', encoding='utf-8') as f:		# файл по стокам
    for line in f:
        data.append(line)


# print(data)

print(type(data), len(data), sys.getsizeof(data)/8, 'Kb')


# print(read_data.find("print(f'-------"))

nomera = []

for i in range(len(data)):
    if "print('------" in data[i]:
        getnumber(data[i])
        nomera.append(i)
        print(data[i])

print(nomera)

ready2print = []

for i in range(len(nomera)):
    print('------------------------------------------------')

    getnumber(data[nomera[i]])

    if i < len(nomera)-1:
        print(data[nomera[i]:nomera[i + 1]])
        ready2print.append([getnumber(data[nomera[i]]), data[nomera[i]:nomera[i + 1]]])
    else:
        print(data[nomera[i]:])
        ready2print.append([getnumber(data[nomera[i]]), data[nomera[i]:]])

print()

#
# for i in ready2print:
#     print(i)
#


for n in range(len(ready2print)):
    print(ready2print[n][0], ready2print[n][1])


    name = 'D:\\code\e\\' + str(ready2print[n][0]) + '.py'
    f = open(name, 'w', encoding='utf-8')

    f.write("# !/usr/bin/python3\n")
    f.write("# -*- coding: utf-8 -*-\n")
    f.write("\n")

    for i in ready2print[n][1]:
        f.write(i)


    f.close()
