print("Change from :-")
print("1 : Kilometer")
print("2 : Meter")
print("3 : Centimeter")
print("4 : Millimeter")
print("5 : Micrometer")
print("6 : Nanometer")
print("7 : Mile")
print("8 : Yard")
print("9 : Foot")
print("10 : Inch")
print("11 : Nautical meter")

from1 = int(input("Enter number:- "))

if from1 == 1:
    print("Convert to:- ")
    print("1 : Meter")
    print("2 : Centimeter")
    print("3 : Millimeter")
    print("4 : Micrometer")
    print("5 : Nanometer")
    print("6 : Mile")
    print("7 : Yard")
    print("8 : Foot")
    print("9 : Inch")
    print("10 : Nautical meter")

    to1 = int(input("Enter number:- "))
    if to1 == 1:
        a = int(input("Enter value:- "))
        print(f"{a} Kilometers = {a*1000} meters")
    elif to1 == 2:
        a = int(input("Enter value:- "))
        print(f"{a} Kilometers = {a*100000} Centimeter")
    elif to1 == 3:
        a = int(input("Enter value:- "))
        print(f"{a} Kilometers = {a*1e+6} Milimeter")       
    elif to1 == 4:
        a = int(input("Enter value:- "))
        print(f"{a} Kilometers = {a*1e+9} Micrometer")
    elif to1 == 5:
        a = int(input("Enter value:- "))
        print(f"{a} Kilometers = {a*1e+12} Nanometer")   
    elif to1 == 6:
        a = int(input("Enter value:- "))
        print(f"{a} Kilometers = {a/1.609} Mile")    
    elif to1 == 7:
        a = int(input("Enter value:- "))
        print(f"{a} Kilometers = {a*1094} Yard")
    elif to1 == 8:
        a = int(input("Enter value:- "))
        print(f"{a} Kilometers = {a*3281} foot")  
    elif to1 == 9:
        a = int(input("Enter value:- "))
        print(f"{a} Kilometers = {a*39370} Inch")    
    elif to1 == 10:
        a = int(input("Enter value:- "))
        print(f"{a} Kilometers = {a/1.852} Nautical meter")                            
    else:
        print("invalid numver")    
elif from1 == 2:
    print("Convert to:- ")
    print("1 : Kilometer")
    print("2 : Centimeter")
    print("3 : Millimeter")
    print("4 : Micrometer")
    print("5 : Nanometer")
    print("6 : Mile")
    print("7 : Yard")
    print("8 : Foot")
    print("9 : Inch")
    print("10 : Nautical meter")

    to1 = int(input("Enter number:- "))
    if to1 == 1:
        a = int(input("Enter value:- "))
        print(f"{a} meters = {a/1000} kilometers")
    elif to1 == 2:
        a = int(input("Enter value:- "))
        print(f"{a} meters = {a*100} Centimeter")
    elif to1 == 3:
        a = int(input("Enter value:- "))
        print(f"{a} meters = {a*1000} Milimeter")       
    elif to1 == 4:
        a = int(input("Enter value:- "))
        print(f"{a} meters = {a*1e+6} Micrometer")
    elif to1 == 5:
        a = int(input("Enter value:- "))
        print(f"{a} meters = {a*1e+9} Nanometer")   
    elif to1 == 6:
        a = int(input("Enter value:- "))
        print(f"{a} meters = {a/1609} Mile")    
    elif to1 == 7:
        a = int(input("Enter value:- "))
        print(f"{a} meters = {a*1.094} Yard")
    elif to1 == 8:
        a = int(input("Enter value:- "))
        print(f"{a} meters = {a*3.281} foot")  
    elif to1 == 9:
        a = int(input("Enter value:- "))
        print(f"{a} meters = {a*39.3701} Inch")    
    elif to1 == 10:
        a = int(input("Enter value:- "))
        print(f"{a} meters = {a/1852} Nautical meter")
    else:
        print("invalid numver") 
elif from1 == 3:
    print("Convert to:- ")
    print("1 : Kilometer")
    print("2 : meter")
    print("3 : Millimeter")
    print("4 : Micrometer")
    print("5 : Nanometer")
    print("6 : Mile")
    print("7 : Yard")
    print("8 : Foot")
    print("9 : Inch")
    print("10 : Nautical meter")

    to1 = int(input("Enter number:- "))
    if to1 == 1:
        a = int(input("Enter value:- "))
        print(f"{a} Centimeters = {a/100000} kilometers")
    elif to1 == 2:
        a = int(input("Enter value:- "))
        print(f"{a} Centimeters = {a/100} meter")
    elif to1 == 3:
        a = int(input("Enter value:- "))
        print(f"{a} Centimeters = {a*10} Milimeter")       
    elif to1 == 4:
        a = int(input("Enter value:- "))
        print(f"{a} Centimeters = {a*10000} Micrometer")
    elif to1 == 5:
        a = int(input("Enter value:- "))
        print(f"{a} Centimeters = {a*1e+7} Nanometer")   
    elif to1 == 6:
        a = int(input("Enter value:- "))
        print(f"{a} Centimeters = {a/160900} Mile")    
    elif to1 == 7:
        a = int(input("Enter value:- "))
        print(f"{a} Centimeters = {a/91.44} Yard")
    elif to1 == 8:
        a = int(input("Enter value:- "))
        print(f"{a} Centimeters = {a/30.48} foot")  
    elif to1 == 9:
        a = int(input("Enter value:- "))
        print(f"{a} Centimeters = {a/2.54} Inch")    
    elif to1 == 10:
        a = int(input("Enter value:- "))
        print(f"{a} Centimeters = {a/185200} Nautical meter")
    else:    
        print("invalid numver")
elif from1 == 4:
    print("Convert to:- ")
    print("1 : Kilometer")
    print("2 : meter")
    print("3 : Centimeter")
    print("4 : Micrometer")
    print("5 : Nanometer")
    print("6 : Mile")
    print("7 : Yard")
    print("8 : Foot")
    print("9 : Inch")
    print("10 : Nautical meter")

    to1 = int(input("Enter number:- "))
    if to1 == 1:
        a = int(input("Enter value:- "))
        print(f"{a} Milimeters = {a/1e+6} kilometers")
    elif to1 == 2:
        a = int(input("Enter value:- "))
        print(f"{a} Milimeters = {a/1000} meter")
    elif to1 == 3:
        a = int(input("Enter value:- "))
        print(f"{a} Milimeters = {a/10} Centimeter")       
    elif to1 == 4:
        a = int(input("Enter value:- "))
        print(f"{a} Milimeters = {a*1000} Micrometer")
    elif to1 == 5:
        a = int(input("Enter value:- "))
        print(f"{a} Milimeters = {a*1e+6} Nanometer")   
    elif to1 == 6:
        a = int(input("Enter value:- "))
        print(f"{a} Milimeters = {a/1.609e+6} Mile")    
    elif to1 == 7:
        a = int(input("Enter value:- "))
        print(f"{a} Milimeters = {a/914.4} Yard")
    elif to1 == 8:
        a = int(input("Enter value:- "))
        print(f"{a} Milimeters = {a/304.8} foot")  
    elif to1 == 9:
        a = int(input("Enter value:- "))
        print(f"{a} Milimeters = {a/25.4} Inch")    
    elif to1 == 10:
        a = int(input("Enter value:- "))
        print(f"{a} Milimeters = {a/1.852e+6} Nautical meter")
    else:    
        print("invalid numver")
elif from1 == 5:
    print("Convert to:- ")
    print("1 : Kilometer")
    print("2 : meter")
    print("3 : Centimeter")
    print("4 : Milimeter")
    print("5 : Nanometer")
    print("6 : Mile")
    print("7 : Yard")
    print("8 : Foot")
    print("9 : Inch")
    print("10 : Nautical meter")

    to1 = int(input("Enter number:- "))
    if to1 == 1:
        a = int(input("Enter value:- "))
        print(f"{a} Micrometers = {a/1e+9} kilometers")
    elif to1 == 2:
        a = int(input("Enter value:- "))
        print(f"{a} Micrometers = {a/1e+6} meter")
    elif to1 == 3:
        a = int(input("Enter value:- "))
        print(f"{a} Micrometers = {a/10000} Centimeter")       
    elif to1 == 4:
        a = int(input("Enter value:- "))
        print(f"{a} Micrometers = {a/1000} Milimeter")
    elif to1 == 5:
        a = int(input("Enter value:- "))
        print(f"{a} Micrometers = {a*1000} Nanometer")   
    elif to1 == 6:
        a = int(input("Enter value:- "))
        print(f"{a} Micrometers = {a/1.609e+9} Mile")    
    elif to1 == 7:
        a = int(input("Enter value:- "))
        print(f"{a} Micrometers = {a/914400} Yard")
    elif to1 == 8:
        a = int(input("Enter value:- "))
        print(f"{a} Micrometers = {a/304800} foot")  
    elif to1 == 9:
        a = int(input("Enter value:- "))
        print(f"{a} Micrometers = {a/25400} Inch")    
    elif to1 == 10:
        a = int(input("Enter value:- "))
        print(f"{a} Micrometers = {a/1.852e+9} Nautical meter")
    else:    
        print("invalid numver")
elif from1 == 6:
    print("Convert to:- ")
    print("1 : Kilometer")
    print("2 : meter")
    print("3 : Centimeter")
    print("4 : Milimeter")
    print("5 : Micrometer")
    print("6 : Mile")
    print("7 : Yard")
    print("8 : Foot")
    print("9 : Inch")
    print("10 : Nautical meter")

    to1 = int(input("Enter number:- "))
    if to1 == 1:
        a = int(input("Enter value:- "))
        print(f"{a} Nanometers = {a/1e+12} kilometers")
    elif to1 == 2:
        a = int(input("Enter value:- "))
        print(f"{a} Nanometers = {a/1e+9} meter")
    elif to1 == 3:
        a = int(input("Enter value:- "))
        print(f"{a} Nanometers = {a/1e+7} Centimeter")       
    elif to1 == 4:
        a = int(input("Enter value:- "))
        print(f"{a} Nanometers = {a/1e+6} Milimeter")
    elif to1 == 5:
        a = int(input("Enter value:- "))
        print(f"{a} Nanometers = {a/1000} Micrometer")   
    elif to1 == 6:
        a = int(input("Enter value:- "))
        print(f"{a} Nanometers = {a/1.609e+12} Mile")    
    elif to1 == 7:
        a = int(input("Enter value:- "))
        print(f"{a} Nanometers = {a/9.144e+8} Yard")
    elif to1 == 8:
        a = int(input("Enter value:- "))
        print(f"{a} Nanometers = {a/3048e+8} foot")  
    elif to1 == 9:
        a = int(input("Enter value:- "))
        print(f"{a} Nanometers = {a/2.54e+7} Inch")    
    elif to1 == 10:
        a = int(input("Enter value:- "))
        print(f"{a} Nanometers = {a/1.852e+12} Nautical meter")
    else:    
        print("invalid numver")
elif from1 == 7:
    print("Convert to:- ")
    print("1 : Kilometer")
    print("2 : meter")
    print("3 : Centimeter")
    print("4 : Milimeter")
    print("5 : Micrometer")
    print("6 : Nanometer")
    print("7 : Yard")
    print("8 : Foot")
    print("9 : Inch")
    print("10 : Nautical meter")

    to1 = int(input("Enter number:- "))
    if to1 == 1:
        a = int(input("Enter value:- "))
        print(f"{a} Mile = {a*1.609} kilometer")
    elif to1 == 2:
        a = int(input("Enter value:- "))
        print(f"{a} Mile = {a/1609} meter")
    elif to1 == 3:
        a = int(input("Enter value:- "))
        print(f"{a} Mile = {a*160900} Centimeter")       
    elif to1 == 4:
        a = int(input("Enter value:- "))
        print(f"{a} Mile = {a*1.609e+6} Milimeter")
    elif to1 == 5:
        a = int(input("Enter value:- "))
        print(f"{a} Mile = {a*1.609e+9} Micrometer")   
    elif to1 == 6:
        a = int(input("Enter value:- "))
        print(f"{a} Mile = {a*1.609e+12} Nanometer")    
    elif to1 == 7:
        a = int(input("Enter value:- "))
        print(f"{a} Mile = {a*1760} Yard")
    elif to1 == 8:
        a = int(input("Enter value:- "))
        print(f"{a} Mile = {a*5280} foot")  
    elif to1 == 9:
        a = int(input("Enter value:- "))
        print(f"{a} Mile = {a*63360} Inch")    
    elif to1 == 10:
        a = int(input("Enter value:- "))
        print(f"{a} Mile = {a/1.156} Nautical meter")
    else:    
        print("invalid numver")
elif from1 == 8:
    print("Convert to:- ")
    print("1 : Kilometer")
    print("2 : meter")
    print("3 : Centimeter")
    print("4 : Milimeter")
    print("5 : Micrometer")
    print("6 : Nanometer")
    print("7 : Mile")
    print("8 : Foot")
    print("9 : Inch")
    print("10 : Nautical meter")

    to1 = int(input("Enter number:- "))
    if to1 == 1:
        a = int(input("Enter value:- "))
        print(f"{a} Yard = {a/1094} kilometer")
    elif to1 == 2:
        a = int(input("Enter value:- "))
        print(f"{a} Yard = {a/1.094} meter")
    elif to1 == 3:
        a = int(input("Enter value:- "))
        print(f"{a} Yard = {a*91.44} Centimeter")       
    elif to1 == 4:
        a = int(input("Enter value:- "))
        print(f"{a} Yard = {a*914.1} Milimeter")
    elif to1 == 5:
        a = int(input("Enter value:- "))
        print(f"{a} Yard = {a*914400} Micrometer")   
    elif to1 == 6:
        a = int(input("Enter value:- "))
        print(f"{a} Yard = {a*9.144e+8} Nanometer")    
    elif to1 == 7:
        a = int(input("Enter value:- "))
        print(f"{a} Yard = {a/1760} Mile")
    elif to1 == 8:
        a = int(input("Enter value:- "))
        print(f"{a} Yard = {a*3} foot")  
    elif to1 == 9:
        a = int(input("Enter value:- "))
        print(f"{a} Yard = {a*36} Inch")    
    elif to1 == 10:
        a = int(input("Enter value:- "))
        print(f"{a} Yard = {a/2025} Nautical meter")
    else:    
        print("invalid numver")
elif from1 == 9:
    print("Convert to:- ")
    print("1 : Kilometer")
    print("2 : meter")
    print("3 : Centimeter")
    print("4 : Milimeter")
    print("5 : Micrometer")
    print("6 : Nanometer")
    print("7 : Mile")
    print("8 : Yard")
    print("9 : Inch")
    print("10 : Nautical meter")

    to1 = int(input("Enter number:- "))
    if to1 == 1:
        a = int(input("Enter value:- "))
        print(f"{a} Foot = {a/3281} kilometer")
    elif to1 == 2:
        a = int(input("Enter value:- "))
        print(f"{a} Foot = {a/3.281} meter")
    elif to1 == 3:
        a = int(input("Enter value:- "))
        print(f"{a} Foot = {a*30.48} Centimeter")       
    elif to1 == 4:
        a = int(input("Enter value:- "))
        print(f"{a} Foot = {a*304.8} Milimeter")
    elif to1 == 5:
        a = int(input("Enter value:- "))
        print(f"{a} Foot = {a*304800} Micrometer")   
    elif to1 == 6:
        a = int(input("Enter value:- "))
        print(f"{a} Foot = {a*3.048e+8} Nanometer")    
    elif to1 == 7:
        a = int(input("Enter value:- "))
        print(f"{a} Foot = {a/5280} Mile")
    elif to1 == 8:
        a = int(input("Enter value:- "))
        print(f"{a} Foot = {a/3} yard")  
    elif to1 == 9:
        a = int(input("Enter value:- "))
        print(f"{a} Foot = {a*12} Inch")    
    elif to1 == 10:
        a = int(input("Enter value:- "))
        print(f"{a} Foot = {a/6076} Nautical meter")
    else:    
        print("invalid numver")
elif from1 == 10:
    print("Convert to:- ")
    print("1 : Kilometer")
    print("2 : meter")
    print("3 : Centimeter")
    print("4 : Milimeter")
    print("5 : Micrometer")
    print("6 : Nanometer")
    print("7 : Mile")
    print("8 : Yard")
    print("9 : Foot")
    print("10 : Nautical meter")

    to1 = int(input("Enter number:- "))
    if to1 == 1:
        a = int(input("Enter value:- "))
        print(f"{a} Inch = {a/39370} kilometer")
    elif to1 == 2:
        a = int(input("Enter value:- "))
        print(f"{a} Inch = {a/39.37} meter")
    elif to1 == 3:
        a = int(input("Enter value:- "))
        print(f"{a} Inch = {a*2.54} Centimeter")       
    elif to1 == 4:
        a = int(input("Enter value:- "))
        print(f"{a} Inch = {a*25.4} Milimeter")
    elif to1 == 5:
        a = int(input("Enter value:- "))
        print(f"{a} Inch = {a*25400} Micrometer")   
    elif to1 == 6:
        a = int(input("Enter value:- "))
        print(f"{a} Inch = {a*2.54e+7} Nanometer")    
    elif to1 == 7:
        a = int(input("Enter value:- "))
        print(f"{a} Inch = {a/63360} Mile")
    elif to1 == 8:
        a = int(input("Enter value:- "))
        print(f"{a} Inch = {a/36} yard")  
    elif to1 == 9:
        a = int(input("Enter value:- "))
        print(f"{a} Inch = {a/12} Foot")    
    elif to1 == 10:
        a = int(input("Enter value:- "))
        print(f"{a} Inch = {a/72910} Nautical meter")
    else:    
        print("invalid numver")
elif from1 == 11:
    print("Convert to:- ")
    print("1 : Kilometer")
    print("2 : meter")
    print("3 : Centimeter")
    print("4 : Milimeter")
    print("5 : Micrometer")
    print("6 : Nanometer")
    print("7 : Mile")
    print("8 : Yard")
    print("9 : Foot")
    print("10 : Nautical meter")

    to1 = int(input("Enter number:- "))
    if to1 == 1:
        a = int(input("Enter value:- "))
        print(f"{a} Nautical meter = {a*1.852} kilometer")
    elif to1 == 2:
        a = int(input("Enter value:- "))
        print(f"{a} Nautical meter = {a*1852} meter")
    elif to1 == 3:
        a = int(input("Enter value:- "))
        print(f"{a} Nautical meter = {a*185200} Centimeter")       
    elif to1 == 4:
        a = int(input("Enter value:- "))
        print(f"{a} Nautical meter = {a*1.852e+6} Milimeter")
    elif to1 == 5:
        a = int(input("Enter value:- "))
        print(f"{a} Nautical meter = {a*1.852e+9} Micrometer")   
    elif to1 == 6:
        a = int(input("Enter value:- "))
        print(f"{a} Nautical meter = {a*1.852e+12} Nanometer")    
    elif to1 == 7:
        a = int(input("Enter value:- "))
        print(f"{a} Nautical meter = {a*1.151} Mile")
    elif to1 == 8:
        a = int(input("Enter value:- "))
        print(f"{a} Nautical meter = {a*2025} yard")  
    elif to1 == 9:
        a = int(input("Enter value:- "))
        print(f"{a} Nautical meter = {a*6076} Foot")    
    elif to1 == 10:
        a = int(input("Enter value:- "))
        print(f"{a} Nautical meter = {a*72910} Inch")
    else:    
        print("invalid numver")              
else:
    print("invalid number")