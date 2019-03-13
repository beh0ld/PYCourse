#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip = input("Enter ip address:")
ip_temp = ip.split('.')

correct_ip = False

while not correct_ip:
    if len(ip_temp) > 4:
        print('Bad address\n')
        ip = input('Enter ip address:')
    for octet in ip_temp:
        if octet > '255' or octet < '0' or octet.isdigit == False:
            print('Bad address\n')
            ip = input('Enter ip address:')
    else:
        correct_ip = True
         
      
if int(ip.split('.')[0]) <= 223 and int(ip.split('.')[0]) > 0:
    print('unicast')
elif int(ip.split('.')[0]) > 223 and int(ip.split('.')[0]) <= 239:
    print('multicast')
elif ip in '255.255.255.255':
    print('local broadcast')
elif ip in '0.0.0.0':
 print('unassigned')
else:
    print('unused')