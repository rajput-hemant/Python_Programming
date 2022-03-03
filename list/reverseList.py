# Python | Reversing a List
list1 = []
n = int(input('Enter the range of the List='))
print('Enter the elements in the list=')
for i in range(n):
    list1.append(int(input()))
print('Your list is=', list1)
print('Reverse list is=[', end='')
for i in range(n, 0, -1):
    print(list1[i-1], end=', ')
print('\b\b]')
