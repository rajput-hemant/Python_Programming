# Python program to check whether the string is Symmetrical or Palindrome
st1 = input('Enter the string=')
if st1[::] == st1[::-1]:
    print(f'The Strings {st1} is palindrome')
elif st1[::] == st1[::]:
    print(f'The String {st1} is Symmetrical')
