#!/usr/bin/python3
def common_elements(set_1, set_2):
    novo_set = {z for z in set_1 if z in set_2}
    return novo_set
