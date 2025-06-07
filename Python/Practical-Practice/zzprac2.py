# # Sample string
# sample_string = "Hello, World! 123"

# # capitalize()
# print(sample_string.capitalize())

# # count()
# print(sample_string.count('l'))

# # endswith()
# print(sample_string.endswith('!'))

# # find()
# print(sample_string.find('World'))

# # index()
# print(sample_string.index('World'))

# # isalnum() - This will return False because of spaces and punctuation in the sample string
# print(sample_string.isalnum())

# # isalpha() - This will return False because of spaces and punctuation in the sample string
# print(sample_string.isalpha())

# # isdigit() - This will return False because there are also letters and punctuation in the sample string
# print(sample_string.isdigit())

# # islower() 
# print(sample_string.islower())

# # isnumeric() - This will return False for similar reasons as isdigit()
# print(sample_string.isnumeric())

# # isspace() - This will return False as there are other characters besides space
# print(sample_string.isspace())

# # isupper()
# print(sample_string.isupper())

# # lower()
# print(sample_string.lower())

# # replace()
# replaced = sample_string.replace("Hello", "Hi")
# print(replaced)

# # rfind()
# position = sample_string.rfind("l")
# if position != -1:
#     print(f"Last occurrence of 'l' found at index {position}")
# else:
#     print("'l' not found")

# rindex_position = sample_string.rindex("l")
# if rindex_position != -1:
#     print(f"Last occurrence of 'l' found at index {rindex_position}")
# else:
#     print("'l' not found")

# # split()
# split_list = sample_string.split(",")
# for item in split_list:a
#     print(item.strip())


# def prime(num):
#     # num = int(input("Enter a number: "))
#     if num == 1:
#         print("is prime")
#     elif num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 print("is not prime")
#                 break
#         else:
#             print("is prime")
#     else:
#         print("is not prime")
# prime(11)


# def fact(n):
#     if n < 0:
#         pass
#     else:
#         # n = int(input("Enter a number: "))
#         m = 1
#         for i in range (2,n+1):
#             m = i * m
#         print(m)
# fact(5)

# from math import pi
# r = 5
# a = pi * r * r 
# print(a)

# import UDModules
# UDModules.add(10,10)

import calendar
y = int(input("yr:- "))
m = int(input("m:- "))
print(calendar.month(y,m))