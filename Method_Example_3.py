class Calculator:
    def __init__(self,model,year):
        self.model = model
        self.year = year

    def add(self,a,b):
        return a+b

    def subtract(self,a,b):
        if a>=b:
            return a-b
        else:
            ValueError("A should be greater than B")

    def multiply(self,a,b):
        return a*b

    def divide(self,a,b):
        if b!=0:
            return a/b
        else:
            ValueError("B should not be 0")


c1=Calculator("ABMODEL",23332)
print(c1.add(2,3))
print(c1.subtract(439,332))
print(c1.subtract(2,3))
print(c1.multiply(3,5))
print(c1.divide(50,5))