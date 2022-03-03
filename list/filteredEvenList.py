# Python program to print even numbers in a list
list1, list2 = [], []
n = int(input('Enter the range of the List='))
print("Enter the elements in the list")
for i in range(n):
    list1.append(int(input()))
print('Your list is=', end=' ')
print(list1)
i = 0
while i != list1[-1]:
    if list1[int(i)] % 2 == 0:
        list2.append(list1[i])
    i += 1
print('Your filtered list with even elements is=', end=' ')
print(list2)
