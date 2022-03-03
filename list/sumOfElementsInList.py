# Python program to find sum of elements in list
list1, add = [], 0
n = int(input('Enter the range of the List='))
print('Enter the elements in the list=')
for i in range(n):
    list1.append(int(input()))
    add = add + list1[i]
print(f'Your list is={list1} and the sum of elements is={add}')
