# Python program to swap two elements in a list
list_for_swapping = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_for_swapping)
print('Enter the position of the elements you want to swap')
n1, n2 = int(input('Position of the first element=')), int(input('Position of the second element='))
list_for_swapping[n1-1], list_for_swapping[n2-1] = list_for_swapping[n2-1], list_for_swapping[n1-1]
print(f'List after swapping {list_for_swapping[n1-1]} with {list_for_swapping[n2-1]} is={list_for_swapping}')
