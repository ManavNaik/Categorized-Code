print("Change from:- ")
print("1. Squre kilometer")
print("2. Squre meter")
print("3. Squre mile")
print("4. Squre foot")
print("5. acer")

from3 = int(input("Enter number:- "))

if from3 == 1:
    print("Change to:- ")
    print("1. Squre meter")
    print("2. Squre mile")
    print("3. Squre foot")
    print("4. acer")

    to3 = int(input("Enter Number:- "))
    if to3 == 1:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Squre Kilometer = {a*1e+6} Squre meter")
    elif to3 == 2:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Squre Kilometer = {a/2.59} Squre mile")
    elif to3 == 3:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Squre Kilometer = {a*1.076e+7} Squre foot")
    elif to3 == 4:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Squre Kilometer = {a*247.1} Acer")
    else:
        print("Invalid number")
elif from3 == 2:
    print("Change to:- ")
    print("1. Squre kilometer")
    print("2. Squre mile")
    print("3. Squre foot")
    print("4. acer")

    to3 = int(input("Enter Number:- "))
    if to3 == 1:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Squre Meter = {a/1e+6} Squre kilometer")
    elif to3 == 2:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Squre Meter = {a/2.59e+6} Squre mile")
    elif to3 == 3:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Squre Meter = {a*10.764} Squre foot")
    elif to3 == 4:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Squre Meter = {a/4047} Acer")
    else:
        print("Invalid number")
elif from3 == 3:
    print("Change to:- ")
    print("1. Squre kilometer")
    print("2. Squre meter")
    print("3. Squre foot")
    print("4. acer")

    to3 = int(input("Enter Number:- "))
    if to3 == 1:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Squre Mile = {a*2.59} Squre kilometer")
    elif to3 == 2:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Squre Mile = {a*2.59e+6} Squre meter")
    elif to3 == 3:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Squre Mile = {a*2.788e+7} Squre foot")
    elif to3 == 4:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Squre Mile = {a*640} Acer")
    else:
        print("Invalid number")
elif from3 == 4:
    print("Change to:- ")
    print("1. Squre kilometer")
    print("2. Squre meter")
    print("3. Squre mile")
    print("4. acer")

    to3 = int(input("Enter Number:- "))
    if to3 == 1:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Squre Foot = {a/1.076e+7} Squre kilometer")
    elif to3 == 2:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Squre Foot = {a/10.764} Squre meter")
    elif to3 == 3:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Squre Foot = {a/2.788e+7} Squre mile")
    elif to3 == 4:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Squre Foot = {a/43560} Acer")
    else:
        print("Invalid number")
elif from3 == 5:
    print("Change to:- ")
    print("1. Squre kilometer")
    print("2. Squre meter")
    print("3. Squre mile")
    print("4. Squre foot")

    to3 = int(input("Enter Number:- "))
    if to3 == 1:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Acre = {a/247.1} Squre kilometer")
    elif to3 == 2:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Acre = {a*4047} Squre meter")
    elif to3 == 3:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Acre = {a/640} Squre mile")
    elif to3 == 4:
        a = int(input("Enter Tonne:- "))
        print(f"{a} Acre = {a*43560} Squre foot")
    else:
        print("Invalid number")
else:
    print("Invalid number")