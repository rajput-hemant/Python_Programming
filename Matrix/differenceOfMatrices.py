# Python | Subtracting Matrices in Python
matrix1, matrix2, matrix3 = [], [], []
print('Enter the dimension of the First Matrix')
r1 = int(input('Enter the no. of rows='))
c1 = int(input('Enter the no. of columns='))
print('Enter the dimension of the Second Matrix')
r2 = int(input('Enter the no. of rows='))
c2 = int(input('Enter the no. of columns='))
if r1 == r2 and c1 == c2:
    print('Enter the elements in the First matrix ROW-WISE=')
    for i in range(r1):
        tmp = []
        for j in range(c1):
            tmp.append(int(input()))
        matrix1.append(tmp)
        print()
    print('Enter the elements in the Second matrix ROW-WISE=')
    for i in range(r2):
        tmp = []
        for j in range(c2):
            tmp.append(int(input()))
        matrix2.append(tmp)
        print()
    for i in range(r1):
        tmp = []
        for j in range(c2):
            tmp.append(0)
        matrix3.append(tmp)
    print('The difference of matrix')
    for i in matrix1:
        print(i)
    print('and')
    for i in matrix2:
        print(i)
    print('is=')
    for i in range(r1):
        for j in range(c1):
            matrix3[i][j] = matrix1[i][j] - matrix2[i][j]
    for i in matrix3:
        print(i)
else:
    print('ERR0R! Dimension of the Matrices are different')
