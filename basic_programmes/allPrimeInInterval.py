# Python program to print all Prime numbers in an Interval
start = int(input("Enter the start of interval="))
end = int(input("Enter the end of the interval="))
print("Prime number between", start, "and", end, "are=")
for i in range(start, end+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
