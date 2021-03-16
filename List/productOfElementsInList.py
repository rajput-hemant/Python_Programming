# Python | Multiply all numbers in the list
list1, product = [], 1
n = int(input('Enter the range of the List='))
print('Enter the elements in the list=')
for i in range(n):
    list1.append(int(input()))
    product *= list1[i]
print(f'Your list is={list1} and the sum of elements is={product}')
