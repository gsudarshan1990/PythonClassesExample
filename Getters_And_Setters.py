class Dog:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name,str):
            self._name = name
        else:
            print("Please enter the correct name")

d1=Dog("jimmy")
print(d1.get_name())
d1.set_name("dimmy")
print(d1.get_name())
d1.set_name(5)