# Python Program for compound interest
p = float(input("Enter the Principal="))
r = float(input("Enter the Rate="))
t = float(input("Enter the Time in years="))
# n = float(input("Enter the number of times the interest is compounded="))
amount = p * (1 + (r/100)) ** t
print("Then compound interest of", p, "at the rate of", r, "% in time", t, "years is", amount - p)
