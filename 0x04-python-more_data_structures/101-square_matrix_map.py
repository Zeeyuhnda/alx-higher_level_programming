#!/usr/bin/python3
def squar_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(lambda i: i ** 2, x)), matrix))
