m = int(input("Enter num:- "))
d = int(input("Enter num:- "))
class Calculator:
    def __init__(self,a,c):
        self.a = a
        self.c = c

    def squre(self):
        print(self.a*self.a)

    def cube(self):
        print(self.a*self.a*self.a)

    def squreRoot(self):
        print(self.a **0.5)

    def addition(self):
        print(self.a+self.c)    

b = Calculator(m,d)
b.squre()
b.cube()
b.squreRoot()
b.addition()




print("Manav")
class proggrammer:
    company = "microsoft"

    def __init__(self,name,product,salare):
        self.name = name
        self.product = product
        self.salare = salare

    def getInfo(self):
        print(f"{self.name},{self.product},{self.salare}")

harry = proggrammer("harry","xbox",200000)
Manav = proggrammer("Manav","windows",500000)
Manav.getInfo()




class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"
    # company = "Youtube"

    def getLanguage(self):
        print(f"The language is {self.language}")
    
    def showDetails(self):
        print("This is an programmer")


e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)