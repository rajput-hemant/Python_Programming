# Python program to count print number of vowels, consonants, digits, or special character in given string
string = input('Enter the String=')
vow, cons, dig, speChar = 0, 0, 0, 0
for i in string:
    if 57 >= ord(i) >= 48:
        dig += 1
    elif i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vow += 1
    elif i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        vow += 1
    elif 90 >= ord(i) >= 65 and (i != 'A' or i != 'E' or i != 'I' or i != 'O' or i != 'U'):
        cons += 1
    elif 122 >= ord(i) >= 97 and (i != 'a' or i != 'e' or i != 'i' or i != 'o' or i != 'u'):
        cons += 1
    else:
        speChar += 1
print(f'In the string {string}\nThe number of Vowels are={vow}\nThe number of Consonants are={cons}')
print(f'The number of Digits are={dig}\nAnd\nThe number of Special Characters are={speChar}')
