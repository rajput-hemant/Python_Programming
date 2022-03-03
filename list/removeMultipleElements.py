# Remove multiple elements from a list in Python
list1 = []
n = int(input('Enter the range of the list='))
print('Enter the elements in the list')
for i in range(n):
    list1.append(int(input()))
print('Your list is=', list1)
tmp = int(input('How many elements you want tot remove?='))
print("Enter the elements you want to remove=")
for i in range(tmp):
    rem = eval(input())
    list1.remove(rem)
print('Your updated list is=', list1)
