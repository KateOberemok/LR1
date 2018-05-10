n = int(input("введите размерность матрицы А:  ")) #вводим число строк матрицы А
answers = 1

#импорт библиотек
import copy
import sys
import math

#импорт методов
from enter_data import *
from nonwoven import *
from lu_decomposition import *
from inverse import *
from cond1 import *
from cond2 import *
from inverse_matrix_gauss import *
from determinant import *

#деление строки на число
def divide_string(str, div):
    for j in range(len(str)):
        str[j] = str[j] / div
    return str

#вычитание из строки другой. умноженной на число
def subtraction_string(str1, str2, multiplier, divident):
    for j in range(len(str1)):
        str2[j] = str2[j] - str1[j] * multiplier / divident
    return str2

#меняем строки местами
def rewriting_row(matrix, first_str, second_str):
    additional_list = matrix[first_str]
    matrix[first_str] = matrix[second_str]
    matrix[second_str] = additional_list
    print(' ')
    print("меняем ", first_str + 1,' и ', second_str + 1, 'строки')
    print(" ")
    print_matrix1(matrix_R)
    return matrix

#обнуляем столбец под диагональю
def straight_run(matrix1, count):
    divident = matrix1[count][count]
    for i in range(n - count - 1):
        multiplier = matrix1[i + count + 1][count]
        subtraction_string(matrix1[count], matrix1[i + count + 1], multiplier, divident)
    print("  ")
    print(count + 1, " шаг")
    print(" ")
    print_matrix1(matrix_R)

#функции вывода на экран
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print('{:>6}'.format(round(matrix[i][j], 3).__str__()), end=' ')
        print("\n")
def print_matrix1(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print('{:>12}'.format(round(matrix[i][j], 20).__str__()), end=' ')
        print("\n")

#инициализация переменных, печать матрицы
matrix_E = identity_matrix(n)
matrix_R = enter_matrix(n)
vector_answers = [0] * n
matrix_test = copy.deepcopy(matrix_R)
matrix_Gauss = copy.deepcopy(matrix_R)
nonw = [0] * n
print(" ")
print_matrix(matrix_R)

#нахождение СЛАУ
ans = input("Вы хотите найти СЛАУ? y/n   ")
if ans == "y":
    for counter in range(n - 1): #прямой ход
        if math.fabs(matrix_R[counter][counter]) > sys.float_info.epsilon*5:
            straight_run(matrix_R, counter)
        else:
            marker = 0
            for k in range(n - counter - 1):
                if matrix_R[counter + k + 1][counter] != 0:
                    rewriting_row(matrix_R, counter, counter + k + 1)
                    marker = 1
            if marker == 1:
                straight_run(matrix_R, counter)
            else:
                answers = 0
                break
    if answers == 0 or matrix_R[n - 1][n - 1] == 0:
        print("ОШИБКА! Матрица вырожденная!")
    else: #обратный ход
        for i in range(n):
            div = matrix_R[n-i-1][n-i-1]
            vector_answers[n-i-1] = matrix_R[n-i-1][n] / div
            for j in range(i):
                vector_answers[n-i-1] = vector_answers[n-i-1] - vector_answers[n-1-j]* matrix_R[n-i-1][n-j-1]/div

        non = nonwoven(matrix_test, vector_answers, nonw)
        for i in range(n):
            for j in range(n):
                matrix_R[i][j] = round(matrix_R[i][j], 2)
        for i in range(n):
            vector_answers[i] = round(vector_answers[i], 2)

        print("  ")
        for i in range(n):
            print("корень x", i + 1," = ", vector_answers[i])

        #нахождение невязки
        ans = input("Вы хотите найти невязку? y/n   ")
        if ans == "y":
            print(" ")
            print("невязка ")
            print( non)
        elif ans == "n":
            print(" ")
        else:
            print(" ")

        #lu разложение
        ans = input("Вы хотите найти разложение LU? y/n   ")
        if ans == "y":
            genegal_lu = lu_decomposition(matrix_test, n)
            if type(genegal_lu) == str:
                print(genegal_lu)
            else:
                print(" ")
                print("матрица U: ")
                u_matrix = zero_matrix(n)
                for i in range(n):
                    u_matrix[i] = genegal_lu[0][i]
                print_matrix(u_matrix)
                print(" ")
                print("матрица L: ")
                l_matrix = zero_matrix(n)
                for i in range(n):
                    l_matrix[i] = genegal_lu[1][i]
                print_matrix(l_matrix)

        #нахождение обратной матрицы
        ans = input("Вы хотите найти обратную матрицу? y/n   ")
        if ans == "y":

            try:
                print(" ")
                print("Обратная матрица ")
                print(" ")
                inv_matrix = inverse(u_matrix, l_matrix, n)
                print_matrix(inv_matrix)
            except:
                print(" ")
                print("Обратная матрица методом Гаусса")
                print_matrix(inverse_matrix_gauss(n, matrix_Gauss))

        # нахождение cond матрицы
        ans = input("Вы хотите найти cond матрицы? y/n   ")
        if ans == "y":
            try:
                print(" ")
                print("cond A (норма 1)")
                number_cond1 = cond1(matrix_test,inverse_matrix_gauss(n, matrix_Gauss) , n)
                print(round(number_cond1, 2))
                print("cond A (норма кубическая)")
                number_cond2 = cond2(matrix_test, inverse_matrix_gauss(n, matrix_Gauss), n)
                print(round(number_cond2, 2))
            except:
                print("")

        # нахождение определителя матрицы
        ans = input("Вы хотите найти детерминант матрицы? y/n   ")
        if ans == "y":
            print(" ")
            print("det A")
            print(determinant(matrix_R, n))
