class Animal:
    def __init__(self,age):
        self.age = age

class Dog(Animal):
    def __init__(self, age, name):
        Animal.__init__(self,age)
        self.name = name

print(issubclass(Dog,Animal))