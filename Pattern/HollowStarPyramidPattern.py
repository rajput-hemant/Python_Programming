# Python program to print Pyramid Using Star Pattern
n = int(input('Enter number of rows='))
i = None
if n == 1:
    print('*')
elif n == 2:
    print(' *')
    print('***')
if n > 2:
    n -= 2
    for i in range(1):
        print(' ' * (n-i) + '*')
    for i in range(1, n+1):
        print(' ' * (n-i) + '*' + ' ' * i + ' ' * (i-1) + '*')
    for i in range(1):
        print('*' * (2*n) + '*')
