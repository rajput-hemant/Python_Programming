# Python program to print Pyramid Using Star Pattern
n = int(input('Enter number of rows='))
i = 0
if n == 1:
    print('*')
elif n == 2:
    print(' *')
    print('***')
if n > 2:
    n -= 2
    print(' ' * (n-i) + '*')
    for i in range(1, n+1):
        print(' ' * (n-i) + '*' + ' ' * i + ' ' * (i-1) + '*')
    print('*' * (2*n) + '*')
