"""A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity.
Suppose, one unit will cost 100. Judge and print total cost for user."""

total_cost = 0
i = 1
while True:
    print(f'Enter the MRP of Product {i}=', end=' ')
    amt = int(input())
    i += 1
    total_cost += amt
    choice = input('Do you want to add another product to your shopping list?\nPress y for YES OR Press n for NO=')
    if choice == 'n':
        break
if total_cost > 1000:
    discount = total_cost//10
    print('You have availed 10% discount on your purchase')
    print('Gross amount=', total_cost)
    print('Discount i.e 10%=', discount)
    print(f'Grand Total={total_cost-discount}₹')
else:
    print(f'Your Bill is Generated\nGrand Total={total_cost}₹')
