# Python program to print all negative numbers in a range
list1 = []
start = int(input('Enter the start of the range of the list='))
stop = int(input('Enter the end of the range of the list='))
print('Enter the elements in the list')
for i in range(start, stop):
    list1.append(i)
print('Your list is=', list1)
print('Negative elements in the range in the list are=', end=' ')
for i in range(start, stop):
    if list1[i] < 0:
        print(list1[i], end=' ')
