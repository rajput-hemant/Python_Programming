# Python | Check if a Substring is Present in a Given String
st1 = input('Enter the string=')
st2 = input('Enter the Substring=')
if st2 in st1:
    print(f"'{st2}' is substring of '{st1}'")
else:
    print(f"'{st2}' is not substring of '{st1}'")
