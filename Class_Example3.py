class Dog:
    def __init__(self,name,age,type):
        self.name=name
        self.age=age
        self.type=type

    def display(self):
        print('{} is name'.format(self.name))

d1=Dog('jimmy',20,'roadside')
d1.display()