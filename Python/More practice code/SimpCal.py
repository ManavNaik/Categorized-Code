print("Select opration you want to perform:-")
print("1 : add")
print("2 : subtract")
print("3 : multiply")
print("4 : divide")

oprator = input("Enter oprator number :- ")

if oprator == "1":
    num1 = int(input("Enter first number:- "))
    num2 = int(input("Enter second number:- "))
    print(f"{num1} + {num2} = {num1 + num2}")
elif oprator == "2":
    num1 = int(input("Enter first number:- "))
    num2 = int(input("Enter second number:- "))
    print(f"{num1} - {num2} = {num1 - num2}")
elif oprator == "3":
    num1 = int(input("Enter first number:- "))
    num2 = int(input("Enter second number:- "))
    print(f"{num1} * {num2} = {num1 * num2}")
elif oprator == "4":
    num1 = int(input("Enter first number:- "))
    num2 = int(input("Enter second number:- "))
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("invalid number")