class Employee:
    def __init__(self,name,age,number,address,vehicle=None):
        self.name = name
        self._age =age
        self.__number = number
        self.__address = address
        self.vehilce = vehicle

e1=Employee("shashank",30,123,2343,"Luna")

print(e1._age)
print(e1._Employee__number)
print(e1._Employee__address)