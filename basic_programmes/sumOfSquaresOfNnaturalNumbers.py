# Python Program for Sum of squares of first n natural numbers
n = int(input('Enter the n='))
add = 0
for i in range(0, n+1):
    add += i**2
print(f'The Sum of squares of first {n} natural numbers is={add}')
