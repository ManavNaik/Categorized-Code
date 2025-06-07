# 3 Write a program to swap the value of two variables

a = int(input("Num 1:- "))
b = int(input("Num 2:- "))
c = a
a = b
b = c
print(f"num 1 :- {a}\nnum 2 :- {b}")


# 8 Print the following patterns using loop :-
# *
# **
# ***
# ****

i = 1
while i<5:
    print("*"*i)
    i = i + 1


# 29 Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
    
uc = 0
lc = 0
s = input("str :- ")
for i in s:
    if i.isupper():
        uc = uc + 1
    else:
        lc = lc + 1
print(f"Upper case :- {uc}\nLower case :- {lc}")


# 37 Write a Python program to create a class to print an integer and a character with two methods having the same name but different sequence of the integer and the character parameters

class eg:
    def val(self,n,c):
        print(n,c)
    def val(self,c,n):
        print(c,n)
obj = eg()
obj.val(5,"M")
obj.val("M",5)