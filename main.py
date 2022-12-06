from function import *

if __name__ == '__main__':
    phonebook_raw = 'phonebook_raw.csv'
    contacts_list = get_csv(phonebook_raw)

    contacts_list_repair = repair_csv(contacts_list)
    new_contact_list = new_csv(contacts_list_repair)

    new_file_csv = 'new_phonebook_raw.csv'
    save_new_csv(new_file_csv, new_contact_list)
