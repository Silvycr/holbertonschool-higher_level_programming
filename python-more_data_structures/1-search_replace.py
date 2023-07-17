#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lista = []
    for xyz in my_list:
        if xyz == search:
            lista.append(replace)
        else:
            lista.append(xyz)
    return lista
