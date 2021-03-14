"""A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount."""

salary = int(input('Hey there Employee!, Please enter your annual income=₹'))
yrs = int(input("Enter the years you've served for the Company="))
if yrs>5:
    bonus = salary//10
    print(f"Thanks for serving the company for all these years\nYou,ve been given a bonus of {bonus}₹")
else:
    print("Dear Employee,\nWe embrace your journey with us\nGreetings")
