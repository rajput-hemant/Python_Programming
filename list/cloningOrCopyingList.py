# Python | Cloning or Copying a list
n = int(input('Enter the range of the List='))
list1 = []
print("Enter the elements in the List=")
for i in range(n):
    list1.append(input())
copy_list = list1
print(f"Your Original list is= {list1}\nYour copied list is={copy_list}")
