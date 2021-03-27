# Python | Count the Number of matching characters in a pair of string
str1 = input('Enter the First string=')
str2 = input('Enter the Second string=')
str3 = ''
str4 = ''
count_char = 0
for i in str1:
    if i not in str3:
        str3 += i
for i in str2:
    if i not in str4:
        str4 += i
for i in str3:
    count = 0
    for j in str4:
        if i == j:
            count += 1
    if count > 0:
        print(f"'{i}'", end=', ')
        count_char += 1
print('\b\b are repeated')
print('No. of matching characters are=', count_char)
