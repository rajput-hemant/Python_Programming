# Python | Remove all duplicates from a given string in Python
str1 = input('Enter the string=')
str2 = str1.split(' ')
str3 = ''
list1 = []
for i in str2:
    if i not in list1:
        list1.append(i)
for i in list1:
    str3 += i + ' '
print(f"Original string='{str1}'\nString after removing duplicates='{str3}\b'")
