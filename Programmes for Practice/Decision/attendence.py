"""
A student will not be allowed to sit in exam if his/her attendance is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
"""

class_held = int(input('Enter the number of classes held='))
class_attended = int(input('Enter the number of class attended='))
attendance = (class_attended/class_held)*100
if attendance > 75:
    print(f'Your attendance percentage is {attendance}%\nHence, You can attend next classes.')
else:
    print(f"Your attendance is {attendance}%, which is below 75%")
    print("Hence, you won't be attending next classes unless you have any medical cause")
    """
    Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has
    medical cause or not ( 'Y' or 'N' ) and print accordingly.
    """
    inp = input("Do you have any medical cause?\nPress 'y' for YES OR press 'n' for NO\n")
    if inp == 'y':
        print('You can attend the classes')
    else:
        print("You can't attend the classes")
