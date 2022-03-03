# Python program to print the sum of n natural number using while loop
n = int(input('Enter the n='))
add, i = 0, 0
while i < n+1:
    add += i
    i += 1
print(f'The sum of all natural numbers till {n} is= {add}')
