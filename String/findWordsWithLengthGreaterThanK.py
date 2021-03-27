# Find words which are greater than given length k
str1 = input('Enter the string=')
str2 = str1.split(' ')
k = int(input("Enter the Word's Length="))
print(f"The words in '{str1}' with word length greater than {k} are=")
for i in str2:
    if len(i) > k:
        print(i)
