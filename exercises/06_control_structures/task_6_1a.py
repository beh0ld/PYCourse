#!/usr/bin/env python3
#-*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ip = input("Enter ip address:")
ip_temp = ip.split('.')

if len(ip_temp) <= 4:
    pass 
else:
    print('Incorrect IPv4 address')   
    quit()
for octet in ip_temp:
    if octet <= '255' and octet >= '0' and octet.isdigit() == True:
        pass   
    else:
        print('Incorrect IPv4 address')   
        quit()
    
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