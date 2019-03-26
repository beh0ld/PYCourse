# -*- coding: utf-8 -*-
'''
Задание 18.1a

Скопировать скрипт add_data.py из задания 18.1.

Добавить в файл add_data.py проверку на наличие БД:
* если файл БД есть, записать данные
* если файла БД нет, вывести сообщение, что БД нет и её необходимо сначала создать

'''
if __name__ == '__main__':
    from create_db import create_db
    from add_data import parse_dhcp_file
    from add_data import add_data
    from add_data import parse_yml_file
    import glob
    from pprint import pprint

    db_filename = 'dhcp_snooping.db'
    schema_filename = 'dhcp_snooping_schema.sql'
    db_connection = create_db(db_filename, schema_filename)
    #print(type(db_connection))

    dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
    print('\nFiles found:')
    print(dhcp_snoop_files)

    dhcp_list = []

    for sw_file in dhcp_snoop_files:
        dhcp_list.extend(parse_dhcp_file(sw_file))

    print('\nParsing result:')
    pprint(dhcp_list)

    sw_list = parse_yml_file('switches.yml')

    print('\nYml read result:')
    pprint(sw_list)

    print('\nInserting DHCP Snooping data')
    add_data(db_connection, dhcp_list, sw_list)