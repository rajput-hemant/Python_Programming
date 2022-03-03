# Python program to print negative numbers in a list
list1 = []
n = int(input('Enter the range of the list='))
print('Enter the elements in the list')
for i in range(n):
    list1.append(int(input()))
print('Your list is=', list1)
print('Positive elements in the list are=', end=' ')
for i in range(n):
    if list1[i] < 0:
        print(list1[i], end=' ')
