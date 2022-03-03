# Python – Convert Snake case to Pascal case
str1 = input('Enter the string in snake_case=')
str2 = str1.split('_')
str3 = ''
for i in str2:
    str3 += i.capitalize()
print(f"snake_case:'{str1}'\nPascalCase:'{str3}'")
