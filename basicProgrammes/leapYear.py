"""
Write a program to check if a year is leap year or not.
"""

year = int(input('Enter the year='))
if 1600 < year < 9999:
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
else:
    print('Please enter valid year!')
