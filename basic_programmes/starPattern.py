###############################
####### Without Boolean #######
###############################

# n = int(input('Enter number of rows='))
# pattern_choice = int(input('Enter 1 to print pattern in ascending order or 0 for descending order='))
# if pattern_choice == 1:
#     for i in range(1, n+1):
#         print('*' * i)
# elif pattern_choice == 0:
#     for i in range(n, 0, -1):
#         print('*' * i)

###############################
######### With Boolean ########
###############################

n = int(input('Enter number of rows='))
pattern_choice = bool(int(input('Enter 1 to print pattern in ascending order or 0 for descending order=')))
if pattern_choice is True:
    for i in range(1, n+1):
        print('*' * i)
elif pattern_choice is False:
    for i in range(n, 0, -1):
        print('*' * i)
