# Python Program for How to check if a given number is Fibonacci number?
n = int(input("Enter a number="))
a = 0
b = 1
total = 0
while total <= n-1:
    a = b
    b = total
    total = a + b
if n == total:
    print(f"{n} is a Fibonacci Number")
else:
    print(f"{n} isn't a Fibonacci Number")
