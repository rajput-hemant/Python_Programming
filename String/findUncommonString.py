# Python program to find uncommon words from two Strings
str1 = input('Enter the First string=')
str2 = input('Enter the second string=')
str3 = str1.split(' ')
str4 = str2.split(' ')
str5, str6 = '', ''
print(f"The uncommon words from '{str1}' and '{str2}' are=")
for i in str3:
    if i not in str4:
        str5 += i + ' '
for i in str4:
    if i not in str3:
        str6 += i + ' '
print(f"'{str5}\b' and '{str6}\b'")
