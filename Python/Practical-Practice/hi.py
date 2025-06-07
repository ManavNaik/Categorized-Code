# # Try - chatch block eg
# class myExc(Exception):
#     pass
# num = -10
# try:
#     if num >= 0 or num <= 101:
#         raise myExc
# except myExc as e:
#     print("Invalid Marks")
# else:
#     print(f"marks obtained {num}")

# class ageE(Exception):
#     pass
# age = 7
# try:
#     if age < 17:
#         raise ageE
# except ageE as e:
#     print("age less then 18")
# else:
#     print(age)


# str = input("Enter str:- ")
# rev_str = str[::-1]
# if str == rev_str:
#     print("palindrome")
# else:
#     print("not a palindrome")


# a = input("1,1")
# b = input("1,2")
# c = input("2,1")
# d = input("2,2")
# l1 = [a,b]
# l2 = [c,d]
# t1 = tuple(l1)
# t2 = tuple(l2)
# t3 = t1
# t1 = t2
# t2 = t3
# print(t1,t2)


# t1 = (30,40)
# t2 = (10,20)
# t3 = t1
# t1 = t2
# t2 = t3
# print(t1,t2)


# class hello:
#     def __init__(self):
#         print("Hello world")
# h = hello()


# with open('first.txt','w') as f:
#     f.write("Hello")
# with open('first.txt', 'r') as f: # Open the first file for reading
#     contents = f.read() # Read the contents of the file
# with open('second.txt', 'w') as f: # Open the second file for writing
#     f.write(contents) 


# a=2
# i=1
# while i < 6:
#     for j in range(i):
#         print(a,end="\t")
#         a+=2
#     i+=2
#     print()