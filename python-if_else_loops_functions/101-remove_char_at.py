#!/usr/bin/python3
def remove_char_at(str, n):
    x = 0
    novo = ""
    for char in str:
        if x != n:
            novo += char
        x += 1
    return (novo)
