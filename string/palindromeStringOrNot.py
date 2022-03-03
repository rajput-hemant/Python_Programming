# Python program to check if a string is palindrome or not
st1 = input('Enter the string=')
if st1[::] == st1[::-1]:
    print(f'The Strings {st1} is palindrome')
else:
    print(f'The Strings {st1} is not palindrome')
