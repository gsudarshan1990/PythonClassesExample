class Calculator:
    def __init__(self,model,year,serial_number):
        self.model = model
        self.year = year
        self.__serial_number = serial_number

    def add(self,a,b):
        return a+b

    def __str__(self):
        return "{} {} {}".format(self.model,self.year,self.__serial_number)


c1=Calculator(100,2020,32323)
print(c1.add(3,2))
print(c1)
c1._Calculator__serial_number=3453442
print(c1)