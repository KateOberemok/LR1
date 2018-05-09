from enter_data import *
import sys
import math

def lu_decomposition(matrix, n):
    marker = 0
    u_matrix = zero_matrix(n)
    l_matrix = zero_matrix(n)
    for count in range(n):
        u_matrix[0][count] = matrix[0][count]
    for count in range(n):
        if math.fabs(u_matrix[0][0]) > sys.float_info.epsilon:
            l_matrix[count][0] = matrix[count][0] / u_matrix[0][0]
        else:
            marker = -1
            break
    for i in range(1, n):
        for j in range(i, n):
            u_matrix[i][j] = matrix[i][j]
            for k in range(0, i):
                u_matrix[i][j] = u_matrix[i][j] - l_matrix[i][k] * u_matrix[k][j]
        for j in range(i, n):
            if math.fabs(u_matrix[i][i]) > sys.float_info.epsilon:
                l_matrix[j][i] = matrix[j][i] / u_matrix[i][i]
                for k in range(i):
                    l_matrix[j][i] -= l_matrix[j][k] * u_matrix[k][i] / u_matrix[i][i]
            else:
                marker = -1
                break
    #for i in range(n):
    #    if u_matrix[i][i] < sys.float_info.epsilon:

    #        marker = -1
    if marker == 0:
        return u_matrix, l_matrix
    else:
        return "LU разложения для этой матрицы нет!"
