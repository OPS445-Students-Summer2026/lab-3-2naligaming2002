#!/usr/bin/env python3

my_list = [1, 2, 3, 4]

def add_item_to_list(lst):
    next_num = max(lst) + 1
    lst.append(next_num)
    lst.append(next_num + 1)
    return lst

def remove_items_from_list(lst, items):
    for item in items:
        if item in lst:
            lst.remove(item)
    return lst
