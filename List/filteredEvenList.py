# Python program to print even numbers in a list
list1, list2 = [], []
print("Enter the elements in the list,type 'esc' to stop")
while True:
    list1.append(input())
    if list1[-1] == "esc":
        list1.remove('esc')
        break
print('Your list is=', end=' ')
print(list1)
i = 0
while i != list1[-1]:
    if list1[int(i)] % 2 == 0:
        list2.append(list1[i])
i += 1
print('Your filtered list with even elements is=', end=' ')
print(list2)
