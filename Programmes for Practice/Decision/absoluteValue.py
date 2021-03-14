"""
Write a program to print absolute value of a number entered by user. E.g.-
INPUT: 1 OUTPUT: 1
INPUT: -1 OUTPUT: 1
"""

while True:
    inp = int(input('Enter the value='))
    print(f"Input: {inp}\t\tOutput: {abs(inp)}")
    choice = input("Wanna run it again?\nPress 'y' for YES OR press 'n' for No=")
    if choice == 'n':
        break
