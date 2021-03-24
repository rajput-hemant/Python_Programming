# Python program to find N largest elements from a list
n = int(input('Enter the range of the List='))
list1, list2 = [], []
print('Enter the elements in the List=')
for i in range(n):
    list1.append(input())
print(f'Your list is={list1}')
tmp = int(input('How many largest elements you want to find?='))
tmp_list = list1
for i in range(tmp):
    lar_ele = max(list1)
    list2.append(lar_ele)
    list1.remove(lar_ele)
print(f"The {tmp} largest elements in the list are={list2}")
