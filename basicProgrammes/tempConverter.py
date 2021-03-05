choice = int(input("Choose what you want to do:\n1). Centigrade->Fahrenheit\n2). Fahrenheit->Centigrade\n"))
temp = int(input("Enter the Temperature="))
if choice == 1:
    print((temp*9/5)+32, "C")
elif choice == 2:
    print((temp-32)*5/9, "F")
