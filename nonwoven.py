def nonwoven(matrix, vector, nonw):
    n = len(vector)

    for counter_row in range(n):

        for counter_coloumn in range(n):
            nonw[counter_row] += matrix[counter_row][counter_coloumn] * vector[counter_coloumn]
        nonw[counter_row] -= matrix[counter_row][n]
    return nonw
