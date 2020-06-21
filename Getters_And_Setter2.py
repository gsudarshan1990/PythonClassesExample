class Dog:
    def __init__(self,age):
        self._age = age
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        if isinstance(age,int):
            self._age =age
        else:
            print("Enter the integer")


d1=Dog(10)
"""
print(d1.get_age())
d1.set_age(20)
print(d1.get_age())
d1.set_age("hellor")
"""

print(d1.age)
d1.age = 30
print(d1.age)


