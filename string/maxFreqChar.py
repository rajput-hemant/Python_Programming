# Python | Maximum frequency character in String
str1 = input("Enter the string=")
char_freq = {}
for i in str1:
    if i in char_freq:
        char_freq[i] += 1
    else:
        char_freq[i] = 1
# For Single Maximum Frequent Character
# print(f"Maximum frequent character in '{str1}' is= {max(char_freq, key=char_freq.get)}")
# For All characters with same frequency
tmp = max(char_freq.values())
list1 = [i for i in char_freq if char_freq[i] == tmp]
print(f"Maximum frequent characters in '{str1}' with same frequency are : " + str(list1))
