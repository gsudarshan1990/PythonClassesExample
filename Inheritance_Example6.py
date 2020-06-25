class Employee:
    salary = 10000
    month_bonus = 500
    def __init__(self,name,age,address,phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone

class Programmer(Employee):
    def __init__(self,name,age,address,phone,programming_language):
        Employee.__init__(self,name,age,address,phone)
        self.program_language=programming_language

class Engineer(Employee):
    def __init__(self,name,age,address,phone,bilingual):
        Employee.__init__(self,name,age,address,phone,bilingual)
        self.bilingual = self.bilingual
