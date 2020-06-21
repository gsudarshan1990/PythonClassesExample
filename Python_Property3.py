class Dog:
    def __init__(self,age):
        self._age = age
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,new_age):
        if isinstance(new_age,int):
            self._age = new_age
        else:
            print('Enter the correct numeric digit')

d1=Dog(10)
print(d1.age)
d1.age = 20
print(d1.age)