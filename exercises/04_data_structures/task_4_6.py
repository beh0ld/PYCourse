# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.replace('[','')
ospf_route = ospf_route.replace(']','')
ospf_route = ospf_route.replace(',','')
ospf_route = ospf_route.replace('O','OSPF')
route = [' Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
ospf = ospf_route.split()
ospf.remove('via')
dict_finish = dict(zip(route,ospf))
finish = str(dict_finish)
finish = finish.replace(',','\n')
finish = finish.replace("'",'')
finish = finish.replace("l:",'l:              ')
finish = finish.replace("x:",'x:                ')
finish = finish.replace("c:",'c:             ')
finish = finish.replace("p:",'p:              ')
finish = finish.replace("te:",'te:           ')
finish = finish.replace("ce:",'ce:        ')
finish = finish.strip('{}')
print(finish)
