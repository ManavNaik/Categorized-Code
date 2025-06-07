print("Change from :-")
print("1 : Bit")
print("2 : Byte")
print("3 : Kilobyte")
print("4 : Megabyte")
print("5 : Gigabyte")
print("6 : terabyte")
print("7 : petabyte")

from1 = int(input("Enter number:- "))

if from1 == 1:
    print("Convert to:- ")
    print("1 : Byte")
    print("2 : Kilobyte")
    print("3 : Megabyte")
    print("4 : Gigabyte")
    print("5 : terabyte")
    print("6 : petabyte")

    to1 = int(input("Enter number:- "))
    if to1 == 1:
        a = int(input("Enter value:- "))
        print(f"{a} Bit = {a/8} Byte")
    elif to1 == 2:
        a = int(input("Enter value:- "))
        print(f"{a} Bit = {a/1000} Kilobyte")
    elif to1 == 3:
        a = int(input("Enter value:- "))
        print(f"{a} Bit = {a/8e+6} Megabyte")       
    elif to1 == 4:
        a = int(input("Enter value:- "))
        print(f"{a} Bit = {a/8e+9} Gigabyte")
    elif to1 == 5:
        a = int(input("Enter value:- "))
        print(f"{a} Bit = {a/8e+12} Terabyte")
    elif to1 == 6:
        a = int(input("Enter value:- "))
        print(f"{a} Bit = {a/8e+15} Petabyte")
    else:
        print("invalid numver")    
elif from1 == 2:
    print("Convert to:- ")
    print("1 : Bit")
    print("2 : Kilobyte")
    print("3 : Megabyte")
    print("4 : Gigabyte")
    print("5 : terabyte")
    print("6 : petabyte")

    to1 = int(input("Enter number:- "))
    if to1 == 1:
        a = int(input("Enter value:- "))
        print(f"{a} Byte = {a*8} Bit")
    elif to1 == 2:
        a = int(input("Enter value:- "))
        print(f"{a} Byte = {a*8000} Kilobyte")
    elif to1 == 3:
        a = int(input("Enter value:- "))
        print(f"{a} Byte = {a/1e+6} Megabyte")       
    elif to1 == 4:
        a = int(input("Enter value:- "))
        print(f"{a} Byte = {a/1e+9} Gigabyte")
    elif to1 == 5:
        a = int(input("Enter value:- "))
        print(f"{a} Byte = {a/1e+12} Terabyte")
    elif to1 == 6:
        a = int(input("Enter value:- "))
        print(f"{a} Byte = {a/1e+15} Petabyte")
    else:
        print("invalid numver")   
elif from1 == 3:
    print("Convert to:- ")
    print("1 : Bit")
    print("2 : Byte")
    print("3 : Megabyte")
    print("4 : Gigabyte")
    print("5 : terabyte")
    print("6 : petabyte")

    to1 = int(input("Enter number:- "))
    if to1 == 1:
        a = int(input("Enter value:- "))
        print(f"{a} kilobyte = {a*8000} Bit")
    elif to1 == 2:
        a = int(input("Enter value:- "))
        print(f"{a} kilobyte = {a*1000} Byte")
    elif to1 == 3:
        a = int(input("Enter value:- "))
        print(f"{a} kilobyte = {a/1000} Megabyte")       
    elif to1 == 4:
        a = int(input("Enter value:- "))
        print(f"{a} kilobyte = {a/1e+6} Gigabyte")
    elif to1 == 5:
        a = int(input("Enter value:- "))
        print(f"{a} kilobyte = {a/1e+9} Terabyte")
    elif to1 == 6:
        a = int(input("Enter value:- "))
        print(f"{a} kilobyte = {a/1e+12} Petabyte")
    else:
        print("invalid numver")  
elif from1 == 4:
    print("Convert to:- ")
    print("1 : Bit")
    print("2 : Byte")
    print("3 : Kilobyte")
    print("4 : Gigabyte")
    print("5 : terabyte")
    print("6 : petabyte")

    to1 = int(input("Enter number:- "))
    if to1 == 1:
        a = int(input("Enter value:- "))
        print(f"{a} Megabyte = {a*8e+6} Bit")
    elif to1 == 2:
        a = int(input("Enter value:- "))
        print(f"{a} Megabyte = {a*1e+6} Byte")
    elif to1 == 3:
        a = int(input("Enter value:- "))
        print(f"{a} Megabyte = {a*1000} Kiobyte")       
    elif to1 == 4:
        a = int(input("Enter value:- "))
        print(f"{a} Megabyte = {a/1000} Gigabyte")
    elif to1 == 5:
        a = int(input("Enter value:- "))
        print(f"{a} Megabyte = {a/1e+6} Terabyte")
    elif to1 == 6:
        a = int(input("Enter value:- "))
        print(f"{a} Megabyte = {a/1e+9} Petabyte")
    else:
        print("invalid numver")  
elif from1 == 5:
    print("Convert to:- ")
    print("1 : Bit")
    print("2 : Byte")
    print("3 : Kilobyte")
    print("4 : Megabyte")
    print("5 : terabyte")
    print("6 : petabyte")

    to1 = int(input("Enter number:- "))
    if to1 == 1:
        a = int(input("Enter value:- "))
        print(f"{a} Gigabyte = {a*8e+9} Bit")
    elif to1 == 2:
        a = int(input("Enter value:- "))
        print(f"{a} Gigabyte = {a*1e+9} Byte")
    elif to1 == 3:
        a = int(input("Enter value:- "))
        print(f"{a} Gigabyte = {a*1e+6} Kiobyte")       
    elif to1 == 4:
        a = int(input("Enter value:- "))
        print(f"{a} Gigabyte = {a*1000} Megabyte")
    elif to1 == 5:
        a = int(input("Enter value:- "))
        print(f"{a} Gigabyte = {a/1000} Terabyte")
    elif to1 == 6:
        a = int(input("Enter value:- "))
        print(f"{a} Gigabyte = {a/1e+6} Petabyte")
    else:
        print("invalid numver")  
elif from1 == 6:
    print("Convert to:- ")
    print("1 : Bit")
    print("2 : Byte")
    print("3 : Kilobyte")
    print("4 : Megabyte")
    print("5 : Gigayte")
    print("6 : Petabyte")

    to1 = int(input("Enter number:- "))
    if to1 == 1:
        a = int(input("Enter value:- "))
        print(f"{a} Terabyte = {a*8e+12} Bit")
    elif to1 == 2:
        a = int(input("Enter value:- "))
        print(f"{a} Terabyte = {a*1e+12} Byte")
    elif to1 == 3:
        a = int(input("Enter value:- "))
        print(f"{a} Terabyte = {a*1e+9} Kiobyte")       
    elif to1 == 4:
        a = int(input("Enter value:- "))
        print(f"{a} Terabyte = {a*1e+6} Megabyte")
    elif to1 == 5:
        a = int(input("Enter value:- "))
        print(f"{a} Terabyte = {a*1000} Gigabyte")
    elif to1 == 6:
        a = int(input("Enter value:- "))
        print(f"{a} Terabyte = {a*1000} Petabyte")
    else:
        print("invalid numver")  
elif from1 == 7:
    print("Convert to:- ")
    print("1 : Bit")
    print("2 : Byte")
    print("3 : Kilobyte")
    print("4 : Megabyte")
    print("5 : Gigayte")
    print("6 : Terabyte")

    to1 = int(input("Enter number:- "))
    if to1 == 1:
        a = int(input("Enter value:- "))
        print(f"{a} Petabyte = {a*8e+15} Bit")
    elif to1 == 2:
        a = int(input("Enter value:- "))
        print(f"{a} Petabyte = {a*1e+15} Byte")
    elif to1 == 3:
        a = int(input("Enter value:- "))
        print(f"{a} Petabyte = {a*1e+12} Kiobyte")       
    elif to1 == 4:
        a = int(input("Enter value:- "))
        print(f"{a} Petabyte = {a*1e+9} Megabyte")
    elif to1 == 5:
        a = int(input("Enter value:- "))
        print(f"{a} Petabyte = {a*1e+6} Gigabyte")
    elif to1 == 6:
        a = int(input("Enter value:- "))
        print(f"{a} Petabyte = {a*1000} Terabyte")
    else:
        print("invalid numver")         
else:
    print("invalid number")