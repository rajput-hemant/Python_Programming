# Python program to find largest number in a list
list1 = []
print("Enter the elements in the list,type 'esc' to stop")
while True:
    list1.append(input())
    if list1[-1] == "esc":
        list1.remove('esc')
        break
print('Your list is=', end=' ')
print(list1)
print("The smallest element in the list is=", max(list1))
