# Python program to print reverse of a number
num = int(input('Enter a four digit number='))
org = num
rev = 0
while num > 0:
    r = num % 10
    rev = rev * 10 + r
    num //= 10
print(f"Input:{org}\t\tOutput:{rev}")