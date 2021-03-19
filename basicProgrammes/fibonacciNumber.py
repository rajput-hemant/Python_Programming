# Python Program for n-th Fibonacci number
n = int(input("Enter a number="))
a = 0
b = 1
total = 0
for i in range(1, n+1):
    if n == 1:
        print(a)
        break
    elif n == 2:
        print(a)
        print(b)
        break
    else:
        print(total)
        a = b
        b = total
        total = a + b
