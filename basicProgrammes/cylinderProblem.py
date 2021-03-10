"""
height of the tank = 10 m
the tank id filling at the rate of 15 metres cube per min
radius of the tank is = 5 m
"""
time = int(input('Enter the Time in minutes='))
height = (15*time)//(3.14*5**2)
if height > 10:
    print(f'The tank is overflowed by {height-10} metres')
elif height == 10:
    print('The tank is full')
elif height < 10:
    print(f'The tank is still empty by {10-height} metres')
