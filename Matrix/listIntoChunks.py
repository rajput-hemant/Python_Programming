# Python | Break a list into chunks of size N in Python
n = int(input('Enter the range of the List='))
list1, tmp, tmp_range = [], 0, 0
print('Enter the elements in the List=')
for i in range(n):
    list1.append(int(input()))
print('Your list is=', list1)
chunk_size = int(input('Enter the chunk size='))
if n % chunk_size == 0:
    tmp_range = len(list1)//chunk_size
elif n % chunk_size != 0:
    tmp_range = (len(list1)//chunk_size)+1
print(f'{list1} is divided into chunks of size {chunk_size}')
for i in range(tmp_range):
    print(list1[tmp:chunk_size])
    tmp = chunk_size
    chunk_size += chunk_size
