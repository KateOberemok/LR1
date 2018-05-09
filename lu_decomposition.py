from enter_data import *
def lu_decomposition(matrix, u_matrix, l_matrix, n):
    for count in range(n):
        u_matrix[0][count] = matrix[0][count]
        #print("u_matrix[o][",count,']', u_matrix[0][count])
    for count in range(n):
        l_matrix[count][0] = matrix[count][0] / u_matrix[0][0]
        #print("l_matrix[", count, '][0]', l_matrix[count][0])
    for i in range(1, n):
        for j in range(i, n):
            u_matrix[i][j] = matrix[i][j]
            #print(u_matrix[i][j])
            for k in range(0, i):
                u_matrix[i][j] = u_matrix[i][j] - l_matrix[i][k] * u_matrix[k][j]
            #print("u_matrix[", i, ']{',j, "]", u_matrix[i][j])
        for j in range(i, n):
            l_matrix[j][i] = matrix[j][i] / u_matrix[i][i]
            for k in range(i):
                l_matrix[j][i] -= l_matrix[j][k] * u_matrix[k][i] / u_matrix[i][i]
            #print("l_matrix[", i, ']{', j, "]", l_matrix[i][j])
    for i in range(n):
        print(u_matrix[i])
    for i in range(n):
        print(l_matrix[i])

m = [[2,2,-1,1],[-3,0,3,0],[-1,3,3,2], [1,0,0,4]]
l = zero_matrix(4)
u = zero_matrix(4)
m2 = [[-5,0,7,0],[4,-24,0,1],[3,12,-7,-23], [-2,42,37,-21]]
lu_decomposition(m,l,u,4)
lu_decomposition(m2,l,u,4)
