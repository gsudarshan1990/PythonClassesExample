class Dog:
    def __init__(self,name,age,color,bloodtype,vaccines):
        self._name = name
        self._age = age
        self._color = color
        self._bloodtype = bloodtype
        self._vaccines = vaccines

class Poodle(Dog):
    def poodle_introduction(self):
        print(f'The name of the dog is {self._name}')

class Schanuzer(Dog):
    def schanuzer_introduction(self):
        print(f'The name of the dog is {self._name}')

my_poodle=Poodle("jimmy",29,"yellow",'red','corona')
my_poodle.poodle_introduction()