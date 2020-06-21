class Dog:
    def __init__(self,number):
        self._number = number

    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self,number):
        if isinstance(number,int):
            self._number = number
        else:
            print("Enter the digits")

d1=Dog(10)
print(d1.number)
d1.number=20
print(d1.number)