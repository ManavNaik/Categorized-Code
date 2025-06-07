print("Change from:- ")
print("1. Miles/hr")
print("2. Foot/Sec")
print("3. Meter/sec")
print("4. Kilometer/sec")
print("5. Knot")

from4 = int(input("Enter number:- "))

if from4 == 1:
    print("Change to:- ")
    print("1. Foot/Sec")
    print("2. Meter/sec")
    print("3. Kilometer/sec")
    print("4. Knot")
    to4 = int(input("Enter number:- "))
    if to4 == 1:
        a = int(input("Enter speed in mile/hr :- "))
        print(f"{a} Mile/hr = {a*1.467} Foot/sec")
    elif to4 == 2:
        a = int(input("Enter speed in mile/hr :- "))
        print(f"{a} Mile/hr = {a/2.237} Meter/sec")
    elif to4 == 3:
        a = int(input("Enter speed in mile/hr :- "))
        print(f"{a} Mile/hr = {a/1.609} Kilometer/sec")
    elif to4 == 4:
        a = int(input("Enter speed in mile/hr :- "))
        print(f"{a} Mile/hr = {a/1.151} Knot")
    else:
        print("Invalid number")
elif from4 == 2:
    print("Change to:- ")
    print("1. Mile/hr")
    print("2. Foot/sec")
    print("3. Kilometer/sec")
    print("4. Knot")
    to4 = int(input("Enter number:- "))
    if to4 == 1:
        a = int(input("Enter speed in foot/sec :- "))
        print(f"{a} Foot/sec = {a/1.467} Mile/hr")
    elif to4 == 2:
        a = int(input("Enter speed in foot/sec :- "))
        print(f"{a} Foot/sec = {a/3.281} Meter/sec")
    elif to4 == 3:
        a = int(input("Enter speed in foot/sec :- "))
        print(f"{a} Foot/sec = {a*1.097} Kilometer/sec")
    elif to4 == 4:
        a = int(input("Enter speed in foot/sec :- "))
        print(f"{a} Foot/sec = {a/1.688} Knot")
    else:
        print("Invalid number")
elif from4 == 3:
    print("Change to:- ")
    print("1. Mile/hr")
    print("2. Meter/sec")
    print("3. Kilometer/sec")
    print("4. Knot")
    to4 = int(input("Enter number:- "))
    if to4 == 1:
        a = int(input("Enter speed in Meter/sec :- "))
        print(f"{a} Meter/sec = {a*2.237} Mile/hr")
    elif to4 == 2:
        a = int(input("Enter speed in Meter/sec :- "))
        print(f"{a} Meter/sec = {a*3.281} Foot/sec")
    elif to4 == 3:
        a = int(input("Enter speed in Meter/sec :- "))
        print(f"{a} Meter/sec = {a*3.6} Kilometer/sec")
    elif to4 == 4:
        a = int(input("Enter speed in Meter/sec :- "))
        print(f"{a} Meter/sec = {a*1.944} Knot")
    else:
        print("Invalid number")
elif from4 == 4:
    print("Change to:- ")
    print("1. Mile/hr")
    print("2. Foot/sec")
    print("3. Meter/sec")
    print("4. Knot")
    to4 = int(input("Enter number:- "))
    if to4 == 1:
        a = int(input("Enter speed in Kilometer/sec :- "))
        print(f"{a} Kilometer/sec = {a*2.237} Mile/hr")
    elif to4 == 2:
        a = int(input("Enter speed in Kilometer/sec :- "))
        print(f"{a} Kilometer/sec = {a*3.281} Foot/sec")
    elif to4 == 3:
        a = int(input("Enter speed in Kilometer/sec :- "))
        print(f"{a} Kilometer/sec = {a*3.6} meter/sec")
    elif to4 == 4:
        a = int(input("Enter speed in Kilometer/sec :- "))
        print(f"{a} Kilometer/sec = {a/1.852} Knot")
    else:
        print("Invalid number")
elif from4 == 5:
    print("Change to:- ")
    print("1. Mile/hr")
    print("2. Foot/sec")
    print("3. Meter/sec")
    print("4. Kilometer")
    to4 = int(input("Enter number:- "))
    if to4 == 1:
        a = int(input("Enter speed in Kilometer/sec :- "))
        print(f"{a} Knot = {a*1.151} Mile/hr")
    elif to4 == 2:
        a = int(input("Enter speed in Kilometer/sec :- "))
        print(f"{a} Knot = {a*1.688} Foot/sec")
    elif to4 == 3:
        a = int(input("Enter speed in Kilometer/sec :- "))
        print(f"{a} Knot = {a/1.944} meter/sec")
    elif to4 == 4:
        a = int(input("Enter speed in Kilometer/sec :- "))
        print(f"{a} Knot = {a*1.852} Kilometer")
    else:
        print("Invalid number")
else:
    print("Invalid number")