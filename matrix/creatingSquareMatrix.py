# Python | Matrix creation of n*n
matrix = []
n = int(input('Enter the value of n for creating n*n Square Matrix='))
print('Enter the elements in the Matrix=')
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(int(input()))
    matrix.append(tmp)
    print()
print('Your Square Matrix is=')
for i in matrix:
    print(i)
