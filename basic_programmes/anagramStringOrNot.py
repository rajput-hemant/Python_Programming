# Python program to check if entered strings are Anagram or Not
string1 = input('Enter the first string=')
string2 = input('Enter the second string=')
if sorted(string1) == sorted(string2):
    print(f'{string1} is an anagram of {string2}')
else:
    print(f'{string1} is not anagram of {string2}')
