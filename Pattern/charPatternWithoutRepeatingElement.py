# Python program to print Character pattern without repeating elements
n = int(input('Enter number of rows='))
ch = 65
for i in range(1, n):
    for j in range(1, i+1):
        print(chr(ch), end=' ')
        ch += 1
    print()
