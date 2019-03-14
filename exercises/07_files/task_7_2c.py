#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv
old_config = argv[1]
new_config = argv[2]

config_cleared = []

with open(old_config, 'r') as f:
    for line in f:
        ignore_line = True in [word in line for word in ignore]
        if not ignore_line:
            config_cleared.append(line)

with open(new_config, 'w') as f:
    f.writelines(config_cleared)