#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    novo_matrix = []
    for y in matrix:
        novo_matrix.append(list(map(lambda x: x ** 2, y)))
    return novo_matrix
