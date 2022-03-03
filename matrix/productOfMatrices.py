# Python program to multiply two matrices
matrix1, matrix2, matrix3 = [], [], []
print('Enter the dimension of the First Matrix')
r1 = int(input('Enter the no. of rows='))
c1 = int(input('Enter the no. of columns='))
print('Enter the dimension of the Second Matrix')
r2 = int(input('Enter the no. of rows='))
c2 = int(input('Enter the no. of columns='))
if r1 == c2:
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
    print('The sum of matrix')
    for i in matrix1:
        print(i)
    print('and')
    for i in matrix2:
        print(i)
    print('is=')
    for i in range(r1):
        for j in range(c2):
            for k in range(c2):
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
    for i in matrix3:
        print(i)
else:
    print('ERR0R! Number of columns of the First Matrix are not equal to the number of the rows of the Second Matrix')
