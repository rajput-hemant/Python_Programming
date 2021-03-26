# Python program to check if a string is palindrome or not
st1 = input('Enter the first string=')
st2 = input('Enter the second string=')
if st1[::] == st2[::-1]:
    print('The Strings are palindrome')
else:
    print('The Strings are not palindrome')
