"""
Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their
place of service.
if employee is female, then she will work only in urban areas.
if employee is a male and age is in between 20 to 40 then he may work in anywhere
if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
And any other input of age should print "ERROR".
"""

age = int(input('Enter your age='))
sex = input("Enter your sex\n'm' for male OR 'f' for female=")
mar_stat = input("Are you married?\n'y' for YES OR 'n' for NO=")
if sex == 'f':
    print("You'll work only in Urban Areas")
elif sex == 'm' and 40 > age > 20:
    print("You can work anywhere")
elif sex == 'm' and 60 > age > 40:
    print("You'll work only in Urban Areas")
else:
    print('ERROR!')
