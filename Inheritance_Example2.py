class Animal:
    sound=""
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("{} makes {} ".format(self.name,self.sound))


class Piglet(Animal):
    sound="oooo"

class Cow(Animal):
    sound="Mink"

piglet=Piglet("Nicky")
cow=Cow("Jinkx")

piglet.speak()
cow.speak()