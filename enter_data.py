def identity_matrix(n): #единичная матрица
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            if i == j:
                matrix[i].append(1)
            else:
                matrix[i].append(0)
    return matrix

def zero_matrix(n): #единичная матрица
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(0)
    return matrix

def enter_matrix(n): #ввод матрицы nxn
    matrix = []
    for i in range(n):
        list = (input("введите " + str(i + 1) + "-ю строку через пробел: ")).split()
        if len(list) != n+1:
            print ("error")
            break
        else:
            for element in range(len(list)):
                list[element] = int(list[element])
            matrix.append(list)
    return matrix
