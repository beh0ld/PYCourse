#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
from sys import argv

config_cleared = []

with open(argv[1], 'r') as f:
    for line in f:
        ignore_line = True in [word in line for word in ignore]
        if not ignore_line:
            config_cleared.append(line)

with open('config_sw1_cleared.txt', 'w') as f:
    f.writelines(config_cleared)