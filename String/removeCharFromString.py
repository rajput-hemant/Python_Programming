# Python program for removing i-th character from a string
str1 = input('Enter the string=')
pos = int(input('Enter the position of the character='))
str2 = str1.replace(str1[pos-1], '', 1)
print(f"'{str1}' after removing char'{str1[pos-1]}' is='{str2}'")
