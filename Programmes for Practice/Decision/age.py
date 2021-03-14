"""
Take input of age of 3 people by user and determine oldest and youngest among them
"""

age1 = int(input('Enter the age of first person='))
age2 = int(input('Enter the age of second person='))
age3 = int(input('Enter the age of third person='))
print(f"The oldest person is {max(age3, age2, age1)} years old ")
print(f"And the youngest person is {min(age3, age2, age1)} years old ")
