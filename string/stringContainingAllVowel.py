# Python program to accept the strings which contains all vowels
str1 = input("Enter the string=")
vowel_list = ['a', 'e', 'i', 'o', 'u']
flag = 0
for i in vowel_list:
    if i not in str1:
        print(f"Vowel {i} not found in the string '{str1}'")
        flag = 1
if flag == 0:
    print(f"The string '{str1}' contains all the vowels.")
