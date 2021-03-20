# Python | Program to print duplicates from a list of integers
n = int(input('Enter the range of the list='))
list1, count, j = [], 0, 0
print('Enter the elements in the List=')
for i in range(n):
    list1.append(int(input()))
print('Your list is=', list1)
print('Duplicates elements are=')
for i in range(n):
    for j in range(i+1, n):
        if list1[i] == list1[j]:
            print(list1[j])
        j += 1
        break
    i += 1
