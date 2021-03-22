# Python program to print Binary Burf Khalifa
n = int(input('Enter the height of the Binary Burj Khalifa='))
ln = len(bin(n))-2
print('How you want to create Binary Burj Khalifa?')
choice = int(input('1:-Right to Left\n2:-Left to Right\n'))
for i in range(n+1):
    if choice == 1:
        # print(f'{{0:>{ln}}}'.format(bin(i)[2:])) # (Shortcut)
        tmp = bin(i)[2:]
        print(' ' * (ln - len(tmp)) + tmp)
    elif choice == 2:
        print(bin(i)[2:])
