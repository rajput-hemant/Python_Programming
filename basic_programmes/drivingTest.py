print("Enter your age=")
age = int(input())
if 7 < age < 100:
    if age > 18:
        print("You can Drive")
    elif age == 18:
        print("You are 18, so you have to give driving test physically")
    else:
        print("You can't Drive")
else:
    print("Please Enter valid age")
