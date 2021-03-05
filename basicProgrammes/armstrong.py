# Python Program to check Armstrong Number
n = int(input("Enter the number="))
arms, tmp, org = int(), int(), n
while n != 0:
    tmp = n % 10
    arms += tmp ** 3
    n //= 10
print("The number is armstrong") if org == arms else print("It's not an armstrong number")
