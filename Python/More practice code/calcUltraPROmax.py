while(True):
    print("")
    print("1. oprations (eg:+,-.)")
    print("2. Length converter")
    print("3. Tables")
    print("4. Temprature converter")
    print("5. Mass converter")
    print("6. Area converter")
    print("7. Speed converter")
    print("8. Data size converter")
    # print("9. Volume converter")
    # print("10. Time converter")
    print("Press q to quit")
    user = input("Enter option's number:- ")
    if user == 'q':
        break
    elif user == 'Manav':
        print("*******************************************\nYOU FOUND AN EATER EGG\n*******************************************")
    try:
        user = int(user)
        if user == 1:
            print("Select opration you want to perform:-")
            print("1 : add")
            print("2 : subtract")
            print("3 : multiply")
            print("4 : divide")
            print("5 : squre")
            print("6 : cube")
            print("7 : squreroot")
            oprator = input("Enter oprator number :- ")
            if oprator == "1":
                num1 = int(input("Enter first number:- "))
                num2 = int(input("Enter second number:- "))
                print(f"{num1} + {num2} = {num1 + num2}")
            elif oprator =="2":
                num1 = int(input("Enter first number:- "))
                num2 = int(input("Enter second number:- "))
                print(f"{num1} - {num2} = {num1 - num2}")
            elif oprator =="3":
                num1 = int(input("Enter first number:- "))
                num2 = int(input("Enter second number:- "))
                print(f"{num1} * {num2} = {num1 * num2}")
            elif oprator =="4":
                num1 = int(input("Enter first number:- "))
                num2 = int(input("Enter second number:- "))
                print(f"{num1} / {num2} = {num1 / num2}")   
            elif oprator =="5":
                num1 = int(input("Enter number:- "))
                print(num1 **2)  
            elif oprator =="6":
                num1 = int(input("Enter number:- "))
                print(num1 **3)  
            elif oprator =="7":
                num1 = int(input("Enter number:- "))
                print(num1 **0.5)     
            else:
                print("invalid number")
        elif user == 2:
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
        elif user == 3:
            a = int(input("Enter any num :- "))
            for i in range (1,11):
                print(f"{a} X {i} = {a*i}")     
        elif user == 4:
            print("Change from:- ")
            print("1. Celsius")
            print("2. Fahernheit")
            print("3. Kelvin")
            from2 = int(input("Enter number:- "))
            if from2 == 1:
                print("Change to:- ")
                print("1. Fahernheit")
                print("2. Kelvin")
                to2 = int(input("Enter °celsius to:- "))
                if to2 == 1:
                    a = int(input("Enter number:- "))
                    print(f"{a}° celsius = {(a* 9/5) + 32}° faheranheite")
                elif to2 == 2:
                    a = int(input("Enter °celsius to:- "))
                    print(f"{a}° celsius = {a + 273.15}° Kelvin")
                else:
                    print("invalid number") 
            elif from2 == 2:
                print("Change to:- ")
                print("1. Celsius")
                print("2. Kelvin")
                to2 = int(input("Enter Number:- "))
                if to2 == 1:
                    a = int(input("Enter °faheranheite to:- "))
                    print(f"{a}° faheranheite = {(a - 32) * 5/9}° celsius")
                elif to2 == 2:
                    a = int(input("Enter °faheranheite to:- "))
                    print(f"{a}° faheranheite = {(a - 32) * 5/9 + 273.15}° Kelvin")
                else:
                    print("invalid number")    
            elif from2 == 3:
                print("Change to:- ")
                print("2. Faheranheite")
                to2 = int(input("Enter Number:- "))
                print("1. Celsius")
                if to2 == 1:
                    a = int(input("Enter °Kelvin to:- "))
                    print(f"{a}° Kelvin = {a - 273.15}° celsius")
                elif to2 == 2:
                    a = int(input("Enter °Kelvin to:- "))
                    print(f"{a}° Kelvin = {(a - 273.15) * 9/5 + 32}° faheranheite")
                else:
                    print("invalid number") 
            else:
                print("Invalid number")
        elif user == 5:
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
                    a = int(input("Enter Grame:- "))
                    print(f"{a} Grame = {a/1e+6} Tonne")
                elif to3 == 2:
                    a = int(input("Enter Grame:- "))
                    print(f"{a} Grame = {a/1000} Kilogram")
                elif to3 == 3:
                    a = int(input("Enter Grame:- "))
                    print(f"{a} Grame = {a*1000} Miligram")
                elif to3 == 4:
                    a = int(input("Enter Grame:- "))
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
                    a = int(input("Enter miligrame:- "))
                    print(f"{a} Miligrame = {a/1e+9} Tonne")
                elif to3 == 2:
                    a = int(input("Enter miligrame:- "))
                    print(f"{a} Miligrame = {a/1e+6} Kilogram")
                elif to3 == 3:
                    a = int(input("Enter miligrame:- "))
                    print(f"{a} Miligrame = {a/1000} gram")
                elif to3 == 4:
                    a = int(input("Enter miligrame:- "))
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
                    a = int(input("Enter pound:- "))
                    print(f"{a} Pound = {a/2205} Tonne")
                elif to3 == 2:
                    a = int(input("Enter pound:- "))
                    print(f"{a} Pound = {a/2.205} Kilogram")
                elif to3 == 3:
                    a = int(input("Enter pound:- "))
                    print(f"{a} Pound = {a*453.6} gram")
                elif to3 == 4:
                    a = int(input("Enter pound:- "))
                    print(f"{a} Pound = {a*453600} Miligram")
                else:
                    print("Invalid number")
            else:
                print("Invalid number")
        elif user == 6:
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
                    a = int(input("Enter Squre Kilometer:- "))
                    print(f"{a} Squre Kilometer = {a*1e+6} Squre meter")
                elif to3 == 2:
                    a = int(input("Enter Squre Kilometer:- "))
                    print(f"{a} Squre Kilometer = {a/2.59} Squre mile")
                elif to3 == 3:
                    a = int(input("Enter Squre Kilometer:- "))
                    print(f"{a} Squre Kilometer = {a*1.076e+7} Squre foot")
                elif to3 == 4:
                    a = int(input("Enter Squre Kilometer:- "))
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
                    a = int(input("Enter Squre meter:- "))
                    print(f"{a} Squre Meter = {a/1e+6} Squre kilometer")
                elif to3 == 2:
                    a = int(input("Enter Squre meter:- "))
                    print(f"{a} Squre Meter = {a/2.59e+6} Squre mile")
                elif to3 == 3:
                    a = int(input("Enter Squre meter:- "))
                    print(f"{a} Squre Meter = {a*10.764} Squre foot")
                elif to3 == 4:
                    a = int(input("Enter Squre meter:- "))
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
                    a = int(input("Enter Squre mile:- "))
                    print(f"{a} Squre Mile = {a*2.59} Squre kilometer")
                elif to3 == 2:
                    a = int(input("Enter Squre mile:- "))
                    print(f"{a} Squre Mile = {a*2.59e+6} Squre meter")
                elif to3 == 3:
                    a = int(input("Enter Squre mile:- "))
                    print(f"{a} Squre Mile = {a*2.788e+7} Squre foot")
                elif to3 == 4:
                    a = int(input("Enter Squre mile:- "))
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
                    a = int(input("Enter Squre foot:- "))
                    print(f"{a} Squre Foot = {a/1.076e+7} Squre kilometer")
                elif to3 == 2:
                    a = int(input("Enter Squre foot:- "))
                    print(f"{a} Squre Foot = {a/10.764} Squre meter")
                elif to3 == 3:
                    a = int(input("Enter Squre foot:- "))
                    print(f"{a} Squre Foot = {a/2.788e+7} Squre mile")
                elif to3 == 4:
                    a = int(input("Enter Squre foot:- "))
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
                    a = int(input("Enter acre:- "))
                    print(f"{a} Acre = {a/247.1} Squre kilometer")
                elif to3 == 2:
                    a = int(input("Enter acre:- "))
                    print(f"{a} Acre = {a*4047} Squre meter")
                elif to3 == 3:
                    a = int(input("Enter acre:- "))
                    print(f"{a} Acre = {a/640} Squre mile")
                elif to3 == 4:
                    a = int(input("Enter acre:- "))
                    print(f"{a} Acre = {a*43560} Squre foot")
                else:
                    print("Invalid number")
            else:
                print("Invalid number")
        elif user == 7:
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
        elif user == 8:
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
        elif user == 9:
            pass
        elif user == 10:
            pass
        else:
            print("Invalid number")
    except:
        print("ENTER A NUMBER")
print("Made by MANAV NAIK")