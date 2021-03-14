"""
A 4 digit number is entered through keyboard. Write a program to print a new number with digits
reversed as of orignal one. E.g.-
INPUT : 1234 OUTPUT : 4321
INPUT : 5982 OUTPUT : 2895

"""

num = int(input('Enter a four digit number='))
org = num
rev = 0
while num > 0:
    r = num % 10
    rev = rev * 10 + r
    num //= 10
print(f"Input:{org}\t\tOutput:{rev}")
