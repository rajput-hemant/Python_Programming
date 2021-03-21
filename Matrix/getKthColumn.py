# Python | Get Kth Column of Matrix
matrix, get_col = [], []
print('Enter the dimension of the Matrix')
r = int(input('Enter the no. of rows='))
c = int(input('Enter the no. of columns='))
print('Enter the elements in the Matrix=')
for i in range(r):
    tmp = []
    for j in range(c):
        tmp.append(int(input()))
    matrix.append(tmp)
    print()
print('Your Matrix is=')
for i in matrix:
    print(i)
k = int(input('Enter the column you want to print='))
if k <= c:
    for i in range(r):
        for j in range(k-1, k):
            get_col.append(matrix[i][j])
    print(f'{k} column of the Matrix is= [', end='')
    for i in get_col:
        print(i, end=', ')
    print('\b\b]')
else:
    print(f'ERR0R! {k} column is not present in the Matrix')
