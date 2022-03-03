# Python program to print Character pattern with Repeating the elements
n = int(input('Enter number of rows='))
for i in range(1, n):
    ch = 65
    for j in range(1, i+1):
        print(chr(ch), end=' ')
        ch += 1
    print()
