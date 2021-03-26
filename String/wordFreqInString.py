# Python – Words Frequency in String Shorthands
str1 = input('Enter the string=')
str2 = str1.split(' ')
list1 = []
for i in str2:
    if i not in list1:
        list1.append(i)
for i in range(len(list1)):
    print('Frequency of', list1[i], 'is :', str1.count(list1[i]))
