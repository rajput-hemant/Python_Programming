# Python program to check whether a number is Prime or not
n = int(input("Enter a number="))
for i in range(2, n):
    if n % i == 0:
        print("Not Prime!")
        break
else:
    print(n, "is a Prime Number")
