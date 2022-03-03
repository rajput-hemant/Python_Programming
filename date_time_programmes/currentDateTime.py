# Python program to get Current Time
import datetime
print(f"Current Date is=[{datetime.date.today()}]")
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"Current Time =[{current_time}]")
# date-time both
# print(datetime.datetime.now())
