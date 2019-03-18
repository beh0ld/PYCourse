# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def get_int_vlan_map(file_name):
    '''
    '''
    dict_access = {}
    dict_trunk = {}

    with open(file_name, 'r') as f:
        for line in f:
            if 'interface' in line:
                interface = line.split()[1]
            elif 'access vlan' in line:
                vlan = int(line.split()[3])
                dict_access[interface] = vlan
            elif 'allowed vlan' in line:
                vlans_list = [int(vlan) for vlan in line.split()[4].split(',')]
                dict_trunk[interface] = vlans_list


    return(dict_access, dict_trunk)

dict_access, dict_trunk = get_int_vlan_map('config_sw1.txt')
