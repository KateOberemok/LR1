from enter_data import *

def vector_y(l_matrix, n, counter):#решение ур-ния Ly = b
    b = [0] * n
    b[counter] = 1
    for i in range(counter + 1, n):
        for j in range(i - counter):
            b[i] -= l_matrix[i][i-j-1]*b[i-j-1]
    return b

def vector_x(u_matrix, n, b):#решение ур-ния Ux = y
    x = [0] *n
    for i in range(n):
        x[n - 1 - i] = b[n - 1 - i]
        for j in range(i):
            x[n - i - 1] -= u_matrix[n - i - 1][n - i + j] * x[n - i + j]
        x[n - i - 1] /= u_matrix[n - i - 1][n - i - 1]
    return x

def inverse(u_matrix, l_matrix, n):
    inverse_matrix = zero_matrix(n)
    for p in range(n):
        x = vector_x(u_matrix, n, vector_y(l_matrix, n, p))
        for q in range(n):
            inverse_matrix[q][p] = x[q]
    return inverse_matrix
