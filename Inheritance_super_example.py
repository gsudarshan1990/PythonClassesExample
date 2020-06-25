class Dog:
    def __init__(self,name):
        self.name = name

class Poodle(Dog):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

P1=Poodle('Nora',5)
