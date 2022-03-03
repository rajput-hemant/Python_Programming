# Python Program for cube sum of first n natural numbers
n = int(input('Enter the n='))
add = 0
for i in range(0, n+1):
    add += i**3
print(add)
