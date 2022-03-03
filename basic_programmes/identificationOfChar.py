ch = input('Enter the character=')
if 'a' <= ch <= 'z':
    print('The character is a lower case alphabet')
elif 'A' <= ch <= 'Z':
    print('The character is Upper case alphabet')
elif '0' <= ch <= '9':
    print('The character is a digit')
else:
    print('It is an Special Character')
