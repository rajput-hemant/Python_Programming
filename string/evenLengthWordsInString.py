# Python program to print even length words in a string
str1 = input("Enter the String=")
list1 = str1.split(" ")
even_len_str = []
for i in list1:
    if len(i) % 2 == 0:
        even_len_str.append(i)
print(f"Even length Words in the String '[{str1}]' are={even_len_str}")
