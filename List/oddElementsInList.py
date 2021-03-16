# Python program to print all odd numbers in a range
list1 = []
n = int(input('Enter the range of the list='))
print('Enter the elements in the list')
for i in range(n):
    list1.append(int(input()))
print('Your list is=', list1)
print('Odd elements in the list are=', end=' ')
for i in range(n):
    if list1[i] % 2 != 0:
        print(list1[i], end=' ')
