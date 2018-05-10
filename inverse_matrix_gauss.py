from enter_data import *

def inverse_matrix_gauss(n, matrix_R):
    matrix_E = identity_matrix(n)
    inverse_matrix = 1

    def print_matrix(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print('{:>6}'.format(round(matrix[i][j], 3).__str__()), end=' ')
            print("\n")

    def divide_string(str, div): #деление строки на число
        for j in range(len(str)):
            str[j] = str[j] / div
        return str

    def subtraction_string(str1, str2, multiplier): #вычитание из строки другой. умноженной на число
        for j in range(len(str1)):
            str2[j] = str2[j] - str1[j] * multiplier
        return str2

    def rewriting_row(matrix, first_str, second_str): #меняем строки местами
        additional_list = matrix[first_str]
        matrix[first_str] = matrix[second_str]
        matrix[second_str] = additional_list
        return matrix

    def straight_run(matrix1, matrix2, count): #обнуляем столбец под диагональю
        divident = matrix1[count][count]
        divide_string(matrix1[count], divident)
        divide_string(matrix2[count], divident)
        for i in range(n - count - 1):
            multiplier = matrix1[i + count + 1][count]
            subtraction_string(matrix1[count], matrix1[i + count + 1], multiplier)
            subtraction_string(matrix2[count], matrix2[i + count + 1], multiplier)


    for counter in range(n): #прямой ход
        if matrix_R[counter][counter] != 0:
            straight_run(matrix_R, matrix_E, counter)
        else:
            marker = 0
            for k in range(n - counter - 1):
                if matrix_R[counter + k + 1][counter] != 0:
                    rewriting_row(matrix_R, counter, counter + k + 1)
                    rewriting_row(matrix_E, counter, counter + k + 1)
                    marker = 1
            if marker == 1:
                straight_run(matrix_R, matrix_E, counter)
            else:
                inverse_matrix = 0
                break

    if inverse_matrix == 1:
        for counter in range(n - 1): #обратный ход
            for i in range(n - counter - 1):
                multiplier = matrix_R[n - i - counter - 2][n - counter - 1]
                subtraction_string(matrix_R[n - counter - 1], matrix_R[n - i - counter - 2], multiplier)
                subtraction_string(matrix_E[n - counter - 1], matrix_E[n - i - counter - 2], multiplier)

        print("")
        return (matrix_E)
    else:
        return ("обратной матрицы нет!")
