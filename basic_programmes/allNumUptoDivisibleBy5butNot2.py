# Python programme to print all numbers upto n which are divisible by 5 but are not divisible by 2
n = int(input('Enter the range='))
print(f'The numbers upto {n} which are divisible by 5 but are not divisible by 2 are=', end=' ')
for i in range(n):
    if i % 5 == 0 and i % 2 != 0:
        print(i, end=', ')
print('\b\b')
