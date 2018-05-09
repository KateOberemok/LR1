from enter_data import *
def lu_decomposition(matrix, u_matrix, l_matrix, n):
    for count in range(n):
        u_matrix[0][count] = matrix[0][count]
    for count in range(n):
        l_matrix[count][0] = matrix[count][0] / u_matrix[0][0]
    for i in range(1, n):
        for j in range(i, n):
            u_matrix[i][j] = matrix[i][j]
            for k in range(i-1):
                u_matrix[i][j] -= l_matrix[j][k] * u_matrix[k][j]
        for j in range(i, n):
            l_matrix[j][i] = matrix[j][i] / u_matrix[i][i]
            for k in range(i-1):
                l_matrix[j][i] -= l_matrix[j][k] * u_matrix[k][i] / u_matrix[i][i]
    for i in range(n):
        print(u_matrix[i])
    for i in range(n):
        print(l_matrix[i])

m = [[1,0,0],[4,3,0],[0,6,9]]
l = zero_matrix(3)
u = zero_matrix(3)

lu_decomposition(m,l,u,3)
