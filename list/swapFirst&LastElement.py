# Python program to interchange first and last elements in a list
print('The original list is=', end=' ')
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(l1)
l1[0], l1[-1] = l1[-1], l1[0]
print('The list after swapping first and last element is=', end=' ')
print(l1)
