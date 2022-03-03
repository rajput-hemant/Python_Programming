# Python Program for factorial of a number
n = int(input("Enter a Number= "))
fact = 1
org = n
while n != 1:
    fact *= n
    n -= 1
print("Factorial of", org, "is=", fact)
