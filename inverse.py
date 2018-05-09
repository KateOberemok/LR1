from enter_data import *
def vector_y(l_matrix, n, counter):
    b = [0] * n
    b[counter] = 1
    for i in range(counter + 1, n):
        for j in range(i - counter):
            b[i] -= l_matrix[i][i-j-1]*b[i-j-1]
    return b

def vector_x(u_matrix, n, b):
    x = [0] *n
    for i in range(n):
        x[n - 1 - i] = b[n - 1 - i]
        for j in range(i):
            x[n - i - 1] -= u_matrix[n - i - 1][n - i + j] * x[n - i + j]
        x[n - i - 1] /= u_matrix[n - i - 1][n - i - 1]
    print(x)
    return x



l_matrix = [[1,0,0],[-12/13,1,0],[4/13,7/5,1]]
u_matrix = [[13,-5,-12],[0,5/13,-144/13],[0,0,-14/5]]

inverse_matrix = zero_matrix(3)

for p in range(3):
    x = vector_x(u_matrix, 3, vector_y(l_matrix, 3, p))
    for q in range(3):
        inverse_matrix[q][p] = x[q]

for i in range(3):
    print(inverse_matrix[i])
