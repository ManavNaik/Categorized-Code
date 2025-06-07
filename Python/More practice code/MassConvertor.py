print("Change from:- ")
print("1. Tonne")
print("2. KiloGram")
print("3. Gram")
print("4. MiliGram")
print("5. Pound")

from3 = int(input("Enter number:- "))

if from3 == 1:
    print("Change to:- ")
    print("1. KiloGram")
    print("2. Gram")
    print("3. MiliGram")
    print("4. Pound")
    to3 = int(input("Enter Number:- "))
    if to3 == 1:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Tonne = {a*1000} Kilogram")
    elif to3 == 2:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Tonne = {a*1e+6} Gram")
    elif to3 == 3:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Tonne = {a*1e+9} Miligram")
    elif to3 == 4:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Tonne = {a*2205} Pound")
    else:
        print("Invalid number")
elif from3 == 2:
    print("Change to:- ")
    print("1. Tonne")
    print("2. Gram")
    print("3. MiliGram")
    print("4. Pound")
    to3 = int(input("Enter Number:- "))
    if to3 == 1:
        a = int(input("Enter Kilograme:- "))
        print(f"{a} Kilograme = {a*1000} Tonne")
    elif to3 == 2:
        a = int(input("Enter Kilograme:- "))
        print(f"{a} Kilograme = {a*1e+6} Gram")
    elif to3 == 3:
        a = int(input("Enter Kilograme:- "))
        print(f"{a} Kilograme = {a*1e+9} Miligram")
    elif to3 == 4:
        a = int(input("Enter Kilograme:- "))
        print(f"{a} Kilograme = {a*2.205} Pound")
    else:
        print("Invalid number")
elif from3 == 3:
    print("Change to:- ")
    print("1. Tonne")
    print("2. Kilogram")
    print("3. MiliGram")
    print("4. Pound")
    to3 = int(input("Enter Number:- "))
    if to3 == 1:
        a = int(input("Enter Kilograme:- "))
        print(f"{a} Grame = {a/1e+6} Tonne")
    elif to3 == 2:
        a = int(input("Enter Kilograme:- "))
        print(f"{a} Grame = {a/1000} Kilogram")
    elif to3 == 3:
        a = int(input("Enter Kilograme:- "))
        print(f"{a} Grame = {a*1000} Miligram")
    elif to3 == 4:
        a = int(input("Enter Kilograme:- "))
        print(f"{a} Grame = {a/453.6} Pound")
    else:
        print("Invalid number")
elif from3 == 4:
    print("Change to:- ")
    print("1. Tonne")
    print("2. Kilogram")
    print("3. MiliGram")
    print("4. Pound")
    to3 = int(input("Enter Number:- "))
    if to3 == 1:
        a = int(input("Enter Kilograme:- "))
        print(f"{a} Miligrame = {a/1e+9} Tonne")
    elif to3 == 2:
        a = int(input("Enter Kilograme:- "))
        print(f"{a} Miligrame = {a/1e+6} Kilogram")
    elif to3 == 3:
        a = int(input("Enter Kilograme:- "))
        print(f"{a} Miligrame = {a/1000} gram")
    elif to3 == 4:
        a = int(input("Enter Kilograme:- "))
        print(f"{a} Miligrame = {a/453600} Pound")
    else:
        print("Invalid number")
elif from3 == 5:
    print("Change to:- ")
    print("1. Tonne")
    print("2. Kilogram")
    print("3. MiliGram")
    print("4. Pound")
    to3 = int(input("Enter Number:- "))
    if to3 == 1:
        a = int(input("Enter Kilograme:- "))
        print(f"{a} Pound = {a/2205} Tonne")
    elif to3 == 2:
        a = int(input("Enter Kilograme:- "))
        print(f"{a} Pound = {a/2.205} Kilogram")
    elif to3 == 3:
        a = int(input("Enter Kilograme:- "))
        print(f"{a} Pound = {a*453.6} gram")
    elif to3 == 4:
        a = int(input("Enter Kilograme:- "))
        print(f"{a} Pound = {a*453600} Miligram")
    else:
        print("Invalid number")
else:
    print("Invalid number")