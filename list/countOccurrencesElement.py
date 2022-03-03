# Python | Count occurrences of an element in a list
n = int(input('Enter the range of the list='))
list1, count = [], 0
print('Enter the elements in the List=')
for i in range(n):
    list1.append(int(input()))
print('Your list is=', list1)
occ = eval(input('Enter the element to check the occurrence='))
for i in range(n):
    if list1[i] == occ:
        count += 1
print(f'The element {occ} has occurred {count} times in the list')
