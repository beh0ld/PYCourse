#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
switchport_mode = input('Enter interface mode (access/trunk):')
interface = input('Enter interface type and number:')
dict_temp = {'access':'Enter VLAN number:', 'trunk': 'Enter allowed VLANs:'}
vlans = input(dict_temp[switchport_mode])
interface = 'interface' + ' ' + interface
dict_acess = dict(enumerate(access_template))
dict_trunk = dict(enumerate(trunk_template))
dict = {'trunk':dict_trunk,'access': dict_acess}
dict = dict.get(switchport_mode)
list_values = list(dict.values())
template = ','.join(list_values)
template = template.replace(',','\n')
print(interface)
print(template.format(vlans))