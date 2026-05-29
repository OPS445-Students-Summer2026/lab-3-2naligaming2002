#!/usr/bin/env python3

my_list = [1, 2, 3, 4]

def add_item_to_list(list_name):

    if max(list_name) < 8:
        list_name.append(max(list_name) + 1)
        list_name.append(max(list_name) + 1)

def remove_items_from_list(list_name, items):

    for item in items:
        if item in list_name:
            list_name.remove(item)

if __name__ == '__main__':
    add_item_to_list(my_list)
    print(my_list)

    remove_items_from_list(my_list, [1, 2])
    print(my_list)
