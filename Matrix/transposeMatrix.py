# Transpose a matrix in Single line in Python
matrix, trans_matrix = [], []
print('Enter the dimension of the Matrix')
r = int(input('Enter the no. of rows='))
c = int(input('Enter the no. of columns='))
print('Enter the elements in the matrix ROW-WISE=')
for i in range(r):
    tmp = []
    for j in range(c):
        tmp.append(int(input()))
    matrix.append(tmp)
    print()
for i in range(c):
    tmp = []
    for j in range(r):
        tmp.append(0)
    trans_matrix.append(tmp)
for i in range(r):
    for j in range(c):
        trans_matrix[j][i] = matrix[i][j]
print('Transpose of the matrix')
for i in matrix:
    print(i)
print('is=')
for i in trans_matrix:
    print(i)
