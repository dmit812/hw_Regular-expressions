import csv
import re


def get_csv(phonebook_raw):
    with open(phonebook_raw, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def save_new_csv(new_phonebook, contacts_list):
    with open(new_phonebook, "w", encoding='utf-8', newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)


pattern_phone_search = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
pattern_phone_sub = r'+7(\2)\3-\4-\5 \6\7'


def repair_csv(file):
    contacts_list = list()
    for data in file:
        result = list()
        full_name = re.findall(r'(\w+)', ' '.join(data[:3]))
        full_name.append('') if len(full_name) < 3 else ...
        result += full_name
        result.append(data[3])
        result.append(data[4])
        result.append(re.sub(pattern_phone_search, pattern_phone_sub, data[5]).strip())
        result.append(data[6])
        contacts_list.append(result)
    return contacts_list


def _del_doubles(one, two):
    result = list()
    for index in range(len(one)):
        result.append(one[index]) if one[index] else result.append(two[index])
    return result


def new_csv(data):
    result = dict()
    for item in data:
        result[item[0]] = _del_doubles(item, result[item[0]]) if item[0] in result else item
    return result.values()
