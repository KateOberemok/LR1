import math

def cond2(matrix, inv_matrix, n):
    matrix_vector = [0] * n
    inv_matrix_vector = [0] * n
    matrix_vector = sum(matrix, matrix_vector)
    inv_matrix_vector = sum(inv_matrix, inv_matrix_vector)
    number_A = maximum(matrix_vector)
    number_inv_A = maximum(inv_matrix_vector)
    cond = number_A * number_inv_A
    return cond

def sum(matrix, vector):
    n = len(vector)
    for i in range(n):
        for j in range(n):
            vector[i] += math.fabs(matrix[i][j])
    return vector

def maximum(vector):
    n = len(vector)
    max = vector[0]
    for i in range(1, n):
        if vector[i] > max:
            max = vector[i]
    return max
