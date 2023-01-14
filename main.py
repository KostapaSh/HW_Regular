import re
import csv
from pprint import pprint


def read_file():

    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    format_FIO(contacts_list)

def format_FIO(contacts):
    fio_contacts_list = []

    fio_pattern = r'^([А-ЯЁа-яё]+)(\s|\,)([А-ЯЁа-яё]+)(\s|\,)([А-ЯЁа-яё]+)(\,)(\,?)(\,?)'
    fio_pattern_sub = r'\1\6\3\6\5\6'

    for fio_list in contacts:
        fio_list_join = ','.join(fio_list)
        fio_list_sub = re.sub(fio_pattern, fio_pattern_sub, fio_list_join)
        fio_contacts_list.append(fio_list_sub.split(','))

    for fio in fio_contacts_list:
        if len(fio[0].split(' ')) > 1:
            fio[1] = fio[0].split(' ')[1]
            fio[0] = fio[0].split(' ')[0]

    format_tel(fio_contacts_list)

def format_tel(contacts):
    tel_contacts_list = []

    tel_pattern = r'(\+7|8)\D*(\d{3})\D*(\d{3})\D*(\d{2})\D*(\d{2})\s*(\(*)(доб.)*(\s*)(\d+)*(\)*)'
    tel_pattern_sub = r'+7(\2)\3-\4-\5 \7\9'

    for tell_list in contacts:
        tel_list_join = ','.join(tell_list)
        tel_list_sub = re.sub(tel_pattern, tel_pattern_sub, tel_list_join)
        tel_contacts_list.append(tel_list_sub.split(','))

    duplicates(tel_contacts_list)

def duplicates(contacts):
    new_contacts_list = []

    for get_fi in contacts:
        for get_fi_com in contacts:
            if get_fi[0] == get_fi_com[0] and get_fi[1] == get_fi_com[1]:
                if get_fi[2] == '':
                    get_fi[2] = get_fi_com[2]
                if get_fi[3] == '':
                    get_fi[3] = get_fi_com[3]
                if get_fi[4] == '':
                    get_fi[4] = get_fi_com[4]
                if get_fi[5] == '':
                    get_fi[5] = get_fi_com[5]
                if get_fi[6] == '':
                    get_fi[6] = get_fi_com[6]

    for new_list in contacts:
        if new_list not in new_contacts_list and len(new_list) < 8:
            new_contacts_list.append(new_list)

    write_file(new_contacts_list)

def write_file(contacts_list):
    with open("phone_book_formatted.csv", "w") as f:
        data_writer = csv.writer(f, delimiter=',')
        data_writer.writerows(contacts_list)

if __name__ == '__main__':
    read_file()
