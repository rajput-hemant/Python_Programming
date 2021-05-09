# Python – Replace multiple words with K
str1 = input("Enter the String=")
print("Enter the Words you want to replace with K=", end=" ")
tmp_list = list(map(str, input().split()))
for i in tmp_list:
    str1 = str1.replace(i, 'k')
print(f"String after replacing {tmp_list} with k is='{str1}'")
