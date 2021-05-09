# Python – Least Frequent Character in String
str1 = input("Enter the string=")
char_freq = {}
for i in str1:
    if i in char_freq:
        char_freq[i] += 1
    else:
        char_freq[i] = 1
print(f"Least frequent character in '{str1}' is= {min(char_freq, key=char_freq.get)}")
