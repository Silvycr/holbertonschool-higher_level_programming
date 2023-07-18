#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nuevo = dict()
    for x, y in a_dictionary.items():
        nuevo[x] = y * 2
    return nuevo
