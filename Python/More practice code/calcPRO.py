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