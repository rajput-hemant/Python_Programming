# Python program to check if year is a Leap Year
year = int(input('Enter the year='))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("It's a Leap Year")
else:
    print("It's not A Leap Year")
