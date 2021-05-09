# Python program to get Current Time
import datetime
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"Current Time =[{current_time}]")
