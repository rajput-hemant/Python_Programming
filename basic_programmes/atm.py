amt = eval(input("Enter then amount="))
f2000 = amt//2000
f500 = amt % 2000
f100 = f500 % 500
f500 //= 500
f100 //= 100
print("₹", amt, "Chiye Ye le ₹2000 k", f2000, "₹500 k", f500, "or ₹ 100 k", f100, "notes")
