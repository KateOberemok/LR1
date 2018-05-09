n = int(input("введите размерность матрицы А:  ")) #вводим число строк матрицы А
answers = 1

import copy
import sys
import math

from enter_data import *
from nonwoven import *


def divide_string(str, div): #деление строки на число
    for j in range(len(str)):
        str[j] = str[j] / div
    return str

def subtraction_string(str1, str2, multiplier, divident): #вычитание из строки другой. умноженной на число
    for j in range(len(str1)):
        str2[j] = str2[j] - str1[j] * multiplier / divident
    return str2

def rewriting_row(matrix, first_str, second_str): #меняем строки местами
    additional_list = matrix[first_str]
    matrix[first_str] = matrix[second_str]
    matrix[second_str] = additional_list
    print(' ')
    print("rewrit ", first_str + 1,' and ', second_str + 1, 'rows')
    for j in range(n):
        print(matrix_R[j])
    return matrix

def straight_run(matrix1, count): #обнуляем столбец под диагональю
    divident = matrix1[count][count]
#    divide_string(matrix1[count], divident)
#    divide_string(matrix2[count], divident)
    for i in range(n - count - 1):
        multiplier = matrix1[i + count + 1][count]
        subtraction_string(matrix1[count], matrix1[i + count + 1], multiplier, divident)
    print("  ")
    print(count + 1, " step")
    for j in range(n):
        print(matrix_R[j])

matrix_E = identity_matrix(n)
matrix_R = enter_matrix(n)
vector_answers = [0] * n
matrix_test = copy.deepcopy(matrix_R)
nonw = [0] * n

for counter in range(n): #прямой ход
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

if answers == 0:
    print("ERROR. Answers didn`t found.")
else:
    for i in range(n):
        div = matrix_R[n-i-1][n-i-1]
        vector_answers[n-i-1] = matrix_R[n-i-1][n] / div
        for j in range(i):
            vector_answers[n-i-1] = vector_answers[n-i-1] - vector_answers[n-1-j]* matrix_R[n-i-1][n-j-1]/div

    for i in range(n):
        for j in range(n):
            matrix_R[i][j] = round(matrix_R[i][j], 2)

    for i in range(n):
        vector_answers[i] = round(vector_answers[i], 2)

    print("  ")
    for i in range(n):
        print("root x", i + 1," = ", vector_answers[i])


    ans = input("Do you want to find non-woven? y/n   ")
    if ans == "y":
        nonwoven(matrix_test, vector_answers, nonw)
        print(" ")
        print("nonwoven ")
        print( nonw)
    elif ans == "n":
        print("ok")
    else:
        print("ok")
