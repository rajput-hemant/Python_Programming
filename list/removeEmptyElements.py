# Python – Remove empty List from List
n = eval(input('Enter the range of the List='))
list1 = []
print('Enter the elements in the List=')
for i in range(n):
    list1.append(str(input()))
print('Your list is=', list1)
print(f"Your updated list without empty elements is={list(filter(None, list1))}")
