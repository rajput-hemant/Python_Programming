# Python | Sum of number digits in List
n = int(input('Enter the range of the List='))
list1, sum1 = [], 0
print('Enter the elements in the List=')
for i in range(n):
    list1.append(eval(input()))
print('Your List is=', list1)
for i in range(n):
    sum1 += list1[i]
print('Sum of number digits in List is=', sum1)
