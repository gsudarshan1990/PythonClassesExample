
class Dog:
    def __init__(self,age):
        self._age =age

    def get_age(self):
        return self._age

    def set_age(self,new_age):
        if isinstance(new_age,int):
            self._age = new_age
        else:
            print('Enter the age in integer')
    age=property(get_age,set_age)

d1=Dog(10)
print(d1.age)
d1.age=20
print(d1.age)