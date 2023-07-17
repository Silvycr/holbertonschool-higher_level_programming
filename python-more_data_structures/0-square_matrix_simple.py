def square_matrix_simple(matrix=[]):
    novo_matrix = []
    for z in matrix:
        novo_matrix.append(list(map(lambda x: x ** 2, z)))
    return novo_matrix
