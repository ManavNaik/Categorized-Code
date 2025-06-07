print("Change from:- ")
print("1. Celsius")
print("2. Fahernheit")
print("3. Kelvin")

from2 = int(input("Enter number:- "))

if from2 == 1:
    print("Change to:- ")
    print("1. Fahernheit")
    print("2. Kelvin")
    to2 = int(input("Enter Number:- "))
    if to2 == 1:
        a = int(input("Enter number:- "))
        print(f"{a}° celsius = {(a* 9/5) + 32}° faheranheite")
    elif to2 == 2:
        a = int(input("Enter number:- "))
        print(f"{a}° celsius = {a + 273.15}° Kelvin")
elif from2 == 2:
    print("Change to:- ")
    print("1. Celsius")
    print("2. Kelvin")
    to2 = int(input("Enter Number:- "))
    if to2 == 1:
        a = int(input("Enter number:- "))
        print(f"{a}° faheranheite = {(a - 32) * 5/9}° celsius")
    elif to2 == 2:
        a = int(input("Enter number:- "))
        print(f"{a}° faheranheite = {(a - 32) * 5/9 + 273.15}° Kelvin")
elif from2 == 3:
    print("Change to:- ")
    print("1. Celsius")
    print("2. Faheranheite")
    to2 = int(input("Enter Number:- "))
    if to2 == 1:
        a = int(input("Enter number:- "))
        print(f"{a}° Kelvin = {a - 273.15}° celsius")
    elif to2 == 2:
        a = int(input("Enter number:- "))
        print(f"{a}° Kelvin = {(a - 273.15) * 9/5 + 32}° faheranheite")
else:
    print("Invalid number")