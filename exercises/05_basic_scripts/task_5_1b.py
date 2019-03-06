#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv
network = str(argv[1:])
network = network.strip('[]')
network = network.strip("")
print(network)
network = network.split('/')
ip = str(network[0])
ip = ip.split('.')
a = int(ip[0])
b = int(ip[1])
c = int(ip[2])
d = int(ip[3])
p = int(network[1])
addr_bits = list(('1'*int(p)).zfill(32))
addr_bits.reverse()
e = int("".join(addr_bits[0:8]))
f = int("".join(addr_bits[8:16]))
g = int("".join(addr_bits[16:24]))
i = int("".join(addr_bits[24:32]))
u = int(("".join(addr_bits[0:8])),2)
k = int(("".join(addr_bits[8:16])),2)
l = int(("".join(addr_bits[16:24])),2)
o = int(("".join(addr_bits[24:32])),2)
network_template = ''' 
         Network:
         {0:<8} {1:<8} {2:<8} {3:<8}
         {0:08b} {1:08b} {2:08b} {3:08b}
         '''
prefix_template = '''
         Mask:
         /{0}
         {5:<8} {6:<8} {7:<8} {8:<8}
         {1:<08} {2:<08} {3:<08} {4:<08}
         '''
print('\n' + '-' * 80)
print(network_template.format(a, b, c, d))
print(prefix_template.format(p, e, f , g, i, u, k, l, o))
print('\n' + '-' * 80)