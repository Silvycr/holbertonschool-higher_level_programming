#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    first_set_1 = {a for a in set_1 if a not in set_2}
    second_set_2 = {a for a in set_2 if a not in set_1}
    return first_set_1 | second_set_2
