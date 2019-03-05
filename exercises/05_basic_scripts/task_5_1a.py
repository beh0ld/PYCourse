# -*- coding: utf-8 -*-
'''
Задание 5.1a

Всё, как в задании 5.1. Но, если пользователь ввел адрес хоста, а не адрес сети,
то надо адрес хоста преобразовать в адрес сети и вывести адрес сети и маску, как в задании 5.1.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
network = input('Enter network(n.n.n.n/n):')
network = input()
print(network)
#network = '172.16.31.0/22'
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
