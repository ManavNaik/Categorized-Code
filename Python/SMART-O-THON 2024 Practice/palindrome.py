#palindrome

str = input("Enter String :- ")
revStr = str[::-1]
if str == revStr:
    print(f"{str} is a palindrome")
else:
    print(f"{str} is not a palindrome")