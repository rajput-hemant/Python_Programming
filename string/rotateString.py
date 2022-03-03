# String slicing in Python to rotate a string
str1 = input("Enter the String=")
tmp = int(input("How you want to rotate the string?\n"
                "1:Left Rotation (Anti-Clockwise)\n"
                "2:Right Rotation (Clockwise)\n"
                "Enter you choice="))
pos = int(input("Enter the position="))
if tmp == 1:
    print(f"Left rotation={str1[pos:]+str1[0:pos]}")
if tmp == 2:
    print(f"Right rotation={str1[len(str1)-pos:]+str1[:len(str1)-pos]}")
