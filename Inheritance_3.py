class Animal:
    sound=""
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("{} and {}".format(self.name,self.sound))

class Piglet(Animal):
    sound="dnajfnas"

class Cow(Animal):
    sound="Minkx"

piglet=Piglet("hello")
cow=Cow("nedls")

piglet.speak()
cow.speak()