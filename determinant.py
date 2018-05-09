def determinant(matrix, n):
    det = 1
    for i in range(n):
        det *= matrix[i][i]
    return det
