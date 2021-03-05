while 1:
    num1 = input("Enter the First Number=")
    num2 = input("Enter the Second Number=")
    num3 = input("Choose the operator\n a). Add\n b). Subt\n c). Mult\n d). Div\n e). Mod\n")
    if int(num1) == 45 and int(num2) == 3 and num3 == "Mult":
        print("555")
    elif int(num1) == 56 and int(num2) == 9 and num3 == "Add":
        print("77")
    elif int(num1) == 56 and int(num2) == 6 and num3 == "Div":
        print("4")
    elif num3 == "Add":
        print(int(num1)+int(num2))
    elif num3 == "Subt":
        print(int(num1)-int(num2))
    elif num3 == "Mult":
        print(int(num1)*int(num2))
    elif num3 == "Div":
        print(int(num1)/int(num2))
    elif num3 == "Mod":
        print(int(num1) % int(num2))
    else:
        print("Unexpected Error! Please check your input")
    choice = input("Do you want to run the calculator again?\n Press y for YES\n Press n for NO\n")
    if choice == "n":
        break
