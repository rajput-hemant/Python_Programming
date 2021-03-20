# Python program to find second largest number in a list
n = int(input('Enter the range of the List='))
list1 = []
print('Enter the elements in the list=')
for i in range(n):
    list1.append(input())
print(f"Your List is= {list1}")
tmp = max(list1)
list1.remove(tmp)
print(f"Second largest element in the List is={max(list1)}")
