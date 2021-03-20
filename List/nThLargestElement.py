# Python program to find N largest elements from a list
n = int(input('Enter the range of the List='))
list1 = []
print('Enter the elements in the List=')
for i in range(n):
    list1.append(input())
print(f'Your list is={list1}')
tmp = int(input('Which largest element you want to find?='))
tmp_list = list1
for i in range(tmp-1):
    lar_ele = max(list1)
    list1.remove(lar_ele)
if tmp == 3:
    print(f'The 3rd largest element in the list is={max(tmp_list)}')
else:
    print(f'The {tmp}th largest element in the list is={max(tmp_list)}')
